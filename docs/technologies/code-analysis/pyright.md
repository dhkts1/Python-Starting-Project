# Pyright - Static Type Checker

Pyright is a fast, accurate static type checker for Python, designed to catch type errors before runtime. It's built by Microsoft and is the type checking engine behind Pylance, the Python language server for VS Code.

## Overview

Pyright analyzes Python code without running it, using type annotations and type inference to detect potential type errors. It's designed to be:

- Fast and scalable, even for large codebases
- Highly configurable to match your project's needs
- Compatible with PEP 484, 526, 544, 561, and other typing-related PEPs
- Usable as a standalone tool or as a VS Code extension

## Installation

Pyright is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pyright
```

## How It's Used in This Project

In this project, Pyright is used to:

1. Verify type correctness of the codebase
2. Catch potential type errors before runtime
3. Enforce type safety standards
4. Provide type information for IDE features

It's configured to run in strict mode, which enforces comprehensive type checking.

## Configuration in This Project

Pyright is configured in the `pyproject.toml` file:

```toml
[tool.pyright]
exclude = [
  "**/__init__.py",
]
include = ["src", "tests"]
pythonVersion = "3.11"
reportUnknownParameterType = "none"
reportUnknownMemberType = "none"
reportUnknownVariableType = "none"
reportUnknownArgumentType = "none"
typeCheckingMode = "strict"
```

This configuration:

- Excludes `__init__.py` files from type checking
- Includes only the `src` and `tests` directories
- Specifies Python 3.11 as the target version
- Disables some specific error reports that might be too noisy
- Enables strict type checking mode

## Basic Usage

### Running Pyright

To run Pyright on the project:

```bash
# Run via poethepoet
uv run poe pyright

# Run directly
uv run pyright
```

### Common Command-Line Options

```bash
# Check specific files or directories
uv run pyright src/specific_module.py

# Show verbose output
uv run pyright --verbose

# Generate a stats file
uv run pyright --stats

# Use a specific Python version
uv run pyright --pythonversion 3.11

# Watch for changes
uv run pyright --watch
```

## Type Annotation Basics

### Variable Annotations

```python
# Variable annotations
name: str = "John"
age: int = 30
is_active: bool = True
```

### Function Annotations

```python
# Function with type annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Function with optional parameters
def greet_optional(name: str, title: str | None = None) -> str:
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"
```

### Class Annotations

```python
# Class with type annotations
class User:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18
```

## Best Practices

1. **Add type annotations to public APIs**: At minimum, annotate function parameters and return types for public functions and methods.
2. **Use type aliases for complex types**: Create type aliases for complex types to improve readability.
3. **Leverage Union types for flexibility**: Use Union types (e.g., `str | None`) for parameters that can accept multiple types.
4. **Use TypedDict for dictionary structures**: Define TypedDict classes for dictionaries with specific structures.
5. **Add Generic types for containers**: Use Generic types for collections to specify contained types.
6. **Gradually add types**: Start with the most critical parts of your codebase and gradually add types to the rest.

## Troubleshooting

### Common Issues

#### Type Errors in Third-Party Libraries

If you get type errors from third-party libraries:

1. Check if type stubs are available: `uv pip install types-package-name`
2. Add the library to the exclude list in `pyproject.toml`
3. Use `# type: ignore` comments for specific imports

#### "Cannot find module" Errors

If Pyright can't find a module:

1. Ensure the module is installed
2. Check your project structure
3. Add the module to the Python path in your configuration

#### "Type is unknown" Errors

If you get "type is unknown" errors:

1. Add type annotations to the relevant variables or functions
2. Use `Any` as a last resort for truly dynamic types
3. Configure specific "reportUnknown\*" settings in `pyproject.toml`

## Resources

- [Pyright Documentation](https://github.com/microsoft/pyright)
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [mypy Type System Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) (also applicable to Pyright)
