# Mkinit - Automatic __init__.py Generator

Mkinit is a Python tool that automatically generates `__init__.py` files for Python packages, making it easier to maintain imports and exports.

## Overview

Mkinit scans Python modules in a package and automatically generates appropriate import statements for the `__init__.py` file. This ensures that all modules and their exports are properly exposed at the package level.

Key features:

- Automatic generation of `__init__.py` files
- Support for lazy loading with lazy_loader
- Generation of typed stub files (`.pyi`)
- Recursive scanning of nested packages
- Customizable import formatting

## Installation

Mkinit is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install mkinit
```

## How It's Used in This Project

In this project, mkinit is used to automatically generate and maintain `__init__.py` files for both the `src` and `tests` directories. This ensures that all modules are properly exposed and can be imported from the package root.

The project configures mkinit to use lazy loading with typed stubs, which improves import performance while maintaining type checking support.

## Configuration in This Project

Mkinit is configured as a poethepoet task in the `pyproject.toml` file:

```toml
[tool.poe.tasks]
mkinit = { sequence = ["mkinit-src", "mkinit-tests"] }
mkinit-src = { cmd = "mkinit src --relative --lazy_loader_typed --black --recursive -w" }
mkinit-tests = { cmd = "mkinit tests --relative --lazy_loader_typed --black --recursive -w" }
```

This configuration:

- Uses relative imports (`--relative`)
- Generates typed lazy loading stubs (`--lazy_loader_typed`)
- Formats the output with Black (`--black`)
- Recursively processes nested packages (`--recursive`)
- Writes the changes to the files (`-w`)

## Basic Usage

### Generating __init__.py Files

To generate `__init__.py` files for the project:

```bash
# Generate for both src and tests
uv run poe mkinit

# Generate only for src
uv run poe mkinit-src

# Generate only for tests
uv run poe mkinit-tests
```

### Manual Usage

You can also run mkinit manually for specific directories:

```bash
# Generate for a specific directory
uv run mkinit path/to/package --relative --recursive -w

# Generate with lazy loading
uv run mkinit path/to/package --lazy_loader -w

# Generate with typed lazy loading
uv run mkinit path/to/package --lazy_loader_typed -w

# Preview changes without writing
uv run mkinit path/to/package
```

## Common Options

Mkinit supports several command-line options:

- `--relative`: Use relative imports instead of absolute imports
- `--recursive`: Process subdirectories recursively
- `--lazy_loader`: Generate lazy loading imports
- `--lazy_loader_typed`: Generate typed lazy loading imports
- `--black`: Format the output with Black
- `-w, --write`: Write changes to the files (otherwise just preview)
- `--diff`: Show a diff of the changes
- `--nomodify`: Don't modify existing imports
- `--nomods`: Don't add import statements for modules

## Best Practices

1. **Run mkinit after adding new modules**: Whenever you add a new module to the project, run mkinit to update the `__init__.py` files.
2. **Use version control**: Always commit `__init__.py` files to version control after generating them.
3. **Include in pre-commit hooks**: Consider adding mkinit to your pre-commit hooks to ensure `__init__.py` files are always up to date.
4. **Use with lazy loading**: Combine mkinit with lazy loading for optimal import performance.

## Troubleshooting

### Common Issues

#### Circular Imports

If you encounter circular import errors:

1. Restructure your code to avoid circular dependencies
2. Use lazy loading to break circular dependencies
3. Use conditional imports inside functions

#### Missing Exports

If some exports are missing from the generated `__init__.py`:

1. Ensure the exports are properly defined in the module
2. Check that the module is in the correct directory
3. Run mkinit with the `--verbose` flag to see what's being processed

## Resources

- [Mkinit Documentation](https://github.com/Erotemic/mkinit)
- [Lazy Loading in Python](https://github.com/scientific-python/lazy_loader)
- [Python Package Structure Best Practices](https://docs.python-guide.org/writing/structure/)
