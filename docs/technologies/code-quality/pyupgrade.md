# Pyupgrade - Python Syntax Upgrader

Pyupgrade is a tool that automatically upgrades your Python syntax to newer versions, helping you take advantage of modern Python features.

## Overview

Pyupgrade scans your Python code for outdated syntax patterns and upgrades them to use newer Python features. It helps:

- Modernize your codebase
- Improve code readability
- Take advantage of performance improvements in newer Python syntax
- Maintain compatibility with specified Python versions

## Installation

Pyupgrade is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pyupgrade
```

## How It's Used in This Project

In this project, Pyupgrade is used to:

1. Automatically upgrade Python syntax to Python 3.11+
1. Maintain modern Python syntax across the codebase
1. Run as part of the pre-commit hooks and CI/CD pipeline

## Configuration in This Project

Pyupgrade is configured as a poethepoet task:

```toml
[tool.poe.tasks]
pyupgrade = "pyupgrade --py311-plus"
```

This configuration specifies that the code should be upgraded to use Python 3.11+ syntax.

## Basic Usage

### Running Pyupgrade

To run Pyupgrade on the project:

```bash
# Run via poethepoet
uv run poe pyupgrade

# Run directly
uv run pyupgrade --py311-plus src/**/*.py
```

### Common Command-Line Options

```bash
# Specify Python version
uv run pyupgrade --py39-plus src/**/*.py

# Keep specific syntax unchanged
uv run pyupgrade --keep-percent-format src/**/*.py

# Run on specific files
uv run pyupgrade path/to/file.py
```

## Examples

### Syntax Upgrades

#### Dictionary Unpacking

Before:

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = dict(list(dict1.items()) + list(dict2.items()))
```

After:

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = {**dict1, **dict2}
```

#### f-strings

Before:

```python
name = "World"
greeting = "Hello, {}!".format(name)
```

After:

```python
name = "World"
greeting = f"Hello, {name}!"
```

#### Type Annotations

Before:

```python
from typing import List, Dict, Optional
names: List[str] = ["Alice", "Bob"]
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}
maybe_name: Optional[str] = None
```

After:

```python
names: list[str] = ["Alice", "Bob"]
ages: dict[str, int] = {"Alice": 30, "Bob": 25}
maybe_name: str | None = None
```

## Best Practices

1. **Run Pyupgrade regularly**: Include Pyupgrade in your pre-commit hooks to ensure consistent syntax.
1. **Specify the correct Python version**: Use the appropriate `--pyXX-plus` flag for your project's minimum Python version.
1. **Combine with other tools**: Use Pyupgrade alongside tools like Ruff and Flynt for comprehensive code modernization.
1. **Review changes**: Some syntax upgrades might change behavior in subtle ways, so review changes carefully.

## Resources

- [Pyupgrade Documentation](https://github.com/asottile/pyupgrade)
- [Python 3.11 What's New](https://docs.python.org/3/whatsnew/3.11.html)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
