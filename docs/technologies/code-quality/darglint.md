# Darglint - Docstring Argument Linter

Darglint is a Python docstring linter that checks whether a docstring's description matches the actual function/method parameters and return values.

## Overview

Darglint helps ensure that your docstrings accurately reflect your code by:

- Verifying that all function parameters are documented
- Checking that documented parameters actually exist in the function signature
- Ensuring return values are properly documented
- Supporting multiple docstring styles (Google, Sphinx, Numpy)
- Integrating with other linting tools

## Installation

Darglint is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install darglint
```

## How It's Used in This Project

In this project, Darglint is used to:

1. Ensure docstrings accurately document function parameters and return values
1. Maintain consistency between code and documentation
1. Run as part of the pre-commit hooks and CI/CD pipeline
1. Improve code quality and maintainability

## Configuration in This Project

Darglint is configured in the `pyproject.toml` file:

```toml
[tool.darglint]
docstring_style = "google"
strictness = "short"
```

This configuration specifies:

- Using Google-style docstrings
- "Short" strictness level, which requires documenting parameters and return values but is lenient on descriptions

## Basic Usage

### Running Darglint

To run Darglint on the project:

```bash
# Run on a specific file
uv run darglint src/your_module.py

# Run on all Python files in a directory
uv run darglint src/
```

### Common Command-Line Options

```bash
# Specify docstring style
uv run darglint --docstring-style=sphinx src/your_module.py

# Set strictness level
uv run darglint --strictness=full src/your_module.py

# Enable/disable specific error codes
uv run darglint --enable=DAR101,DAR102 src/your_module.py
uv run darglint --disable=DAR003 src/your_module.py
```

## Examples

### Google-style Docstring (Passing)

```python
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b
```

### Google-style Docstring (Failing)

```python
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result.

    Args:
        a: The first number.
        c: This parameter doesn't exist!  # Darglint will flag this

    # Missing documentation for parameter 'b'
    # Missing Returns section
    """
    return a + b
```

## Error Codes

| Code | Description |
|--------|-------------------------------------------------------|
| DAR001 | Missing parameter in docstring |
| DAR002 | Excess parameter in docstring |
| DAR003 | Missing return in docstring |
| DAR004 | Excess return in docstring |
| DAR101 | Missing parameter description in docstring |
| DAR102 | Excess parameter description in docstring |
| DAR103 | Missing return description in docstring |
| DAR104 | Excess return description in docstring |
| DAR201 | Missing "Yields" in docstring for generator function |
| DAR202 | Excess "Yields" in docstring for non-generator function |
| DAR301 | Missing "Raises" in docstring for function that raises|
| DAR302 | Excess "Raises" in docstring for function that doesn't raise |

## Best Practices

1. **Keep docstrings up to date**: Update docstrings whenever you change function signatures.
1. **Be consistent with style**: Choose one docstring style (Google, Sphinx, or Numpy) and stick with it.
1. **Document all parameters**: Include descriptions for all function parameters.
1. **Document return values**: Always specify what your function returns.
1. **Document exceptions**: Use the "Raises" section to document exceptions your function might raise.
1. **Run Darglint regularly**: Include Darglint in your pre-commit hooks to catch issues early.

## Resources

- [Darglint Documentation](https://github.com/terrencepreilly/darglint)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
