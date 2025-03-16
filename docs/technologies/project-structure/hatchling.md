# Hatchling - Modern Python Project Build Backend

Hatchling is a modern, extensible build backend for Python projects that simplifies packaging, building, and distribution while providing powerful customization options.

## Overview

Hatchling helps manage Python project builds by:

- Providing a modern, standards-compliant build system
- Supporting dynamic version management
- Offering a plugin system for customization
- Enabling metadata customization
- Supporting various project structures
- Integrating with the Python packaging ecosystem
- Working seamlessly with other tools like pip, uv, and PyPI

## Installation

Hatchling is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install hatchling
```

## How It's Used in This Project

In this project, Hatchling is used to:

1. Define the project's build system
2. Manage package metadata
3. Handle version information
4. Configure package discovery and inclusion
5. Support the build and distribution process

## Configuration in This Project

Hatchling is configured in the `pyproject.toml` file:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "your-package-name"
version = "0.1.0"
description = "Your package description"
readme = "README.md"
requires-python = ">=3.11"
license = { text = "MIT" }
authors = [
  { name = "Your Name", email = "your.email@example.com" },
]
dependencies = [
  # List of dependencies
]

[tool.hatch.build.targets.wheel]
packages = ["src/your_package"]
```

## Basic Usage

### Building a Package

To build a package using Hatchling:

```bash
# Build a wheel
uv run hatch build

# Build a source distribution
uv run hatch build --target sdist

# Build both wheel and sdist
uv run hatch build --target wheel --target sdist
```

### Publishing a Package

```bash
# Build and publish to PyPI
uv run hatch publish

# Build and publish to TestPyPI
uv run hatch publish --repo test
```

## Examples

### Dynamic Version Management

```toml
[tool.hatch.version]
path = "src/your_package/__about__.py"
```

With `__about__.py` containing:

```python
__version__ = "0.1.0"
```

### Custom Package Discovery

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/your_package"]
```

### Conditional Dependencies

```toml
[project.optional-dependencies]
dev = [
  "pytest>=7.0.0",
  "pytest-cov>=4.1.0",
]
docs = [
  "mkdocs>=1.4.0",
  "mkdocs-material>=9.0.0",
]
```

## Build Process

When you run `hatch build`, Hatchling performs these steps:

1. **Configuration Loading**: Reads the `pyproject.toml` file
2. **Version Resolution**: Determines the package version
3. **Metadata Preparation**: Prepares package metadata
4. **Source Processing**: Processes source files according to configuration
5. **Build Execution**: Creates the distribution packages (wheel, sdist)
6. **Artifact Generation**: Outputs the final distribution files

## Best Practices

1. **Use src layout**: Place your package code in a `src` directory for cleaner separation.
2. **Specify Python version**: Always set the `requires-python` field to ensure compatibility.
3. **Include a README**: Provide a README.md file for PyPI display.
4. **Manage versions properly**: Use a single source of truth for version information.
5. **Define optional dependencies**: Group dependencies logically using optional-dependencies.
6. **Include license information**: Always specify license information in your project metadata.
7. **Use dynamic metadata**: Take advantage of Hatchling's dynamic metadata capabilities for complex projects.

## Advanced Features

### Environment Markers

```toml
[project]
dependencies = [
  "importlib-metadata>=4.6; python_version < '3.10'",
  "tomli>=2.0.0; python_version < '3.11'",
]
```

### Hooks and Plugins

```toml
[tool.hatch.build.hooks.custom]
path = "build_hooks.py"
```

With a custom hook in `build_hooks.py`:

```python
def hook(version, build_data, artifacts):
    # Custom build logic here
    return artifacts
```

## Resources

- [Hatchling Documentation](https://hatch.pypa.io/latest/plugins/build-hook/hatchling/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [PEP 621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
- [PyPI Publishing Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
