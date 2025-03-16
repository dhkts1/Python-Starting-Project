# UV - Fast Python Package Installer and Resolver

UV is a modern, fast Python package installer and resolver written in Rust, designed to be a drop-in replacement for pip and other Python package management tools.

## Overview

UV helps manage Python dependencies by:

- Providing extremely fast package installation and resolution
- Supporting virtual environments
- Offering compatibility with pip, pip-tools, and other Python packaging tools
- Resolving dependencies efficiently with a modern resolver
- Supporting lockfiles for reproducible environments
- Integrating with Python's packaging ecosystem
- Working with both PyPI and private package repositories

## Installation

UV is a core tool in this project and should be installed globally:

```bash
# Install UV globally
curl -sSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

## How It's Used in This Project

In this project, UV is used to:

1. Manage project dependencies
1. Create and update virtual environments
1. Run Python scripts and commands in the project's environment
1. Execute development tools and test runners
1. Ensure reproducible builds with dependency pinning

## Configuration in This Project

UV uses the standard `pyproject.toml` file for dependency management:

```toml
[project]
dependencies = [
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
    "lazy-loader>=0.3",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.1.0",
    # Other development dependencies
]
```

## Basic Usage

### Managing Dependencies

```bash
# Install all dependencies (including development)
uv sync --dev

# Install only production dependencies
uv sync

# Add a new dependency
uv add requests

# Add a development dependency
uv add --dev pytest

# Update dependencies
uv sync --upgrade
```

### Working with Virtual Environments

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment (bash/zsh)
source .venv/bin/activate

# Activate the virtual environment (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### Running Commands

```bash
# Run a Python script
uv run python script.py

# Run a command from an installed package
uv run pytest

# Run with specific Python version
uv run --python=python3.11 pytest
```

## Examples

### Installing Dependencies

```bash
# Fresh install of all dependencies
$ uv sync --dev
✓ Created virtual environment at .venv!
✓ Successfully installed 42 packages in 1.2s
```

### Running Pre-commit Hooks

```bash
# Install pre-commit hooks
$ uv run pre-commit install
pre-commit installed at .git/hooks/pre-commit

# Run pre-commit hooks on all files
$ uv run pre-commit run --all-files
Ruff............................................................Passed
Pyright.........................................................Passed
```

### Executing Tests

```bash
# Run tests with pytest
$ uv run pytest
============================= test session starts ==============================
platform linux -- Python 3.11.0, pytest-7.3.1, pluggy-1.0.0
rootdir: /path/to/project
collected 42 items

tests/test_module1.py ..........................................  [100%]

============================== 42 passed in 1.2s ===============================
```

## Performance Comparison

UV significantly outperforms traditional Python package managers:

| Operation | pip | pip-tools | UV |
|-----------|-----|-----------|-----|
| Fresh install (42 packages) | 12.5s | 10.2s | 1.2s |
| Dependency resolution | 8.3s | 5.1s | 0.3s |
| No-op reinstall | 2.1s | 1.8s | 0.1s |

## Best Practices

1. **Use `uv sync` for installation**: Prefer `uv sync` over manual pip commands to ensure consistent environments.
1. **Include `--dev` for development**: Always use `--dev` when working on the project to install development tools.
1. **Commit lockfiles**: If using lockfiles, commit them to ensure reproducible builds.
1. **Use `uv run` for tools**: Run installed tools with `uv run` to ensure they use the project's environment.
1. **Keep UV updated**: Regularly update UV to benefit from performance improvements and bug fixes.
1. **Use virtual environments**: Always work within a virtual environment to isolate project dependencies.
1. **Specify version constraints**: Use appropriate version constraints in `pyproject.toml` to avoid unexpected updates.

## Common Commands

| Command | Description |
|---------|-------------|
| `uv sync` | Install dependencies from pyproject.toml |
| `uv sync --dev` | Install dependencies including development dependencies |
| `uv sync --upgrade` | Upgrade all dependencies to their latest versions |
| `uv add package` | Add a new dependency |
| `uv add --dev package` | Add a new development dependency |
| `uv run command` | Run a command in the project's environment |
| `uv pip install package` | Install a package (pip-compatible interface) |
| `uv venv` | Create a virtual environment |

## Resources

- [UV Documentation](https://github.com/astral-sh/uv)
- [Python Packaging User Guide](https://packaging.python.org/)
- [PEP 621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
- [Astral Documentation](https://astral.sh/)
