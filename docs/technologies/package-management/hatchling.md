# Hatchling - Modern Python Build System

Hatchling is a modern, extensible build backend for Python projects. It's designed to be a replacement for setuptools, offering a more modern and flexible approach to building Python packages.

## Overview

Hatchling is the build backend for the Hatch project management tool, but it can be used independently. It provides:

- A modern build system for Python packages
- Support for dynamic metadata
- Plugin system for extending functionality
- PEP 517/518 compliance

## How It's Used in This Project

In this project, Hatchling is used as the build backend for creating distributable packages. It's configured in the `pyproject.toml` file:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

The project also configures Hatchling's wheel builder:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src", "tests"]
```

This configuration ensures that both the `src` and `tests` directories are included in the built wheel.

## Building Packages

To build packages using Hatchling:

```bash
# Build a wheel
uv run python -m build --wheel

# Build both wheel and sdist
uv run python -m build
```

## Configuration Options

Hatchling offers many configuration options in `pyproject.toml`:

### Basic Project Metadata

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "Project description"
readme = "README.md"
requires-python = ">=3.11"
license = { text = "MIT" }
authors = [
  { name = "Your Name", email = "your.email@example.com" },
]
```

### Dependencies

```toml
[project]
dependencies = [
  "dependency1>=1.0.0",
  "dependency2>=2.0.0",
]

[project.optional-dependencies]
dev = [
  "pytest>=7.0.0",
  "black>=23.0.0",
]
```

### Entry Points

```toml
[project.scripts]
command-name = "package.module:function"

[project.gui-scripts]
gui-command = "package.module:function"

[project.entry-points."package.plugins"]
plugin-name = "package.module:function"
```

### Build Configuration

```toml
[tool.hatch.build]
exclude = [
  "tests/",
  "docs/",
]

[tool.hatch.build.targets.wheel]
packages = ["src"]
```

## Best Practices

1. **Use `src` directory structure**: This keeps your package code separate from project files.
2. **Specify Python version requirements**: Use `requires-python` to ensure compatibility.
3. **Include comprehensive metadata**: Provide complete project information for better PyPI presentation.
4. **Use dynamic versioning when appropriate**: Hatchling supports various versioning schemes.

## Troubleshooting

### Common Issues

#### Build Fails with Missing Dependencies

If the build fails due to missing dependencies:

```bash
# Install build dependencies
uv pip install build hatchling

# Try building again
uv run python -m build
```

#### Package Missing Files

If the built package is missing files:

1. Check the `[tool.hatch.build.targets.wheel]` section
2. Ensure all necessary directories are included
3. Check for exclude patterns that might be too broad

## Resources

- [Hatchling Documentation](https://hatch.pypa.io/latest/build/)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [PEP 517 - Build System Interface](https://peps.python.org/pep-0517/)
- [PEP 518 - Build System Requirements](https://peps.python.org/pep-0518/)
