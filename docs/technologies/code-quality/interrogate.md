# Interrogate - Docstring Coverage Checker

Interrogate is a Python tool that checks your codebase for missing docstrings, helping you maintain comprehensive documentation across your project.

## Overview

Interrogate helps improve code documentation by:

- Measuring docstring coverage in your codebase
- Identifying modules, classes, methods, and functions missing docstrings
- Generating detailed reports on documentation status
- Supporting various output formats (terminal, badge, etc.)
- Integrating with CI/CD pipelines and pre-commit hooks
- Allowing customization through configuration options

## Installation

Interrogate is included as a development dependency:

```bash linenums="1"
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash linenums="1"
uv pip install interrogate
```

## How It's Used in This Project

In this project, Interrogate is used to:

1. Ensure all modules, classes, methods, and functions have docstrings
1. Maintain a high level of documentation coverage
1. Run as part of the pre-commit hooks and CI/CD pipeline
1. Generate coverage reports for documentation quality assessment

## Configuration in This Project

Interrogate is configured in the `pyproject.toml` file:

```toml linenums="1"
[tool.interrogate]
ignore-init-method = true  # (1)
ignore-init-module = true
ignore-magic = true
ignore-semiprivate = true
ignore-private = true
ignore-property-decorators = true
ignore-module = true
ignore-nested-functions = true
ignore-nested-classes = true
fail-under = 95  # (2)
exclude = ["tests", "docs", "build", "dist"]  # (3)
verbose = 1
quiet = false
whitelist-regex = []
color = true
```

1. Ignores special methods that typically don't need docstrings
1. Requires at least 95% docstring coverage to pass
1. Excludes test files, documentation, and build artifacts from analysis

This configuration:

- Ignores certain types of methods and modules that typically don't need docstrings
- Requires at least 95% docstring coverage
- Excludes test files, documentation, and build artifacts
- Enables colored output for better readability

## Basic Usage

### Running Interrogate

To run Interrogate on the project:

=== "Using poe tasks"
`bash linenums="1"     # Run via poethepoet     uv run poe docstring-check     `

=== "Using direct commands"
\`\`\`bash linenums="1"
\# Run on the entire project
uv run interrogate src/

````
# Run with detailed output
uv run interrogate -v src/

# Generate a badge for README
uv run interrogate -v -b src/
```
````

### Common Command-Line Options

```bash linenums="1"
# Set minimum coverage threshold
uv run interrogate --fail-under=90 src/

# Exclude specific directories
uv run interrogate --exclude="tests,docs" src/

# Generate a badge
uv run interrogate --badge src/

# Output results as JSON
uv run interrogate --output-format=json src/
```

## Examples

### Terminal Output

```text linenums="1"
RESULT: PASSED (minimum: 95.0%, actual: 98.7%)

src/your_package/__init__.py: 100.0%
src/your_package/module1.py: 100.0%
src/your_package/module2.py: 95.5%
src/your_package/utils.py: 100.0%

TOTAL: 98.7%
```

### Badge Generation

```bash linenums="1"
$ uv run interrogate -b src/
RESULT: PASSED (minimum: 95.0%, actual: 98.7%)
Wrote badge to: ./interrogate_badge.svg
```

## Coverage Levels

Interrogate measures docstring coverage at different levels:

1. **Module-level**: Docstrings at the top of Python files
1. **Class-level**: Docstrings for class definitions
1. **Method/Function-level**: Docstrings for methods and functions
1. **Nested-level**: Docstrings for nested classes and functions (if configured)

## Best Practices

1. **Write docstrings for all public APIs**: Ensure all public classes, methods, and functions have docstrings.
1. **Use a consistent docstring style**: Follow a standard format like Google, NumPy, or reStructuredText.
1. **Include examples in docstrings**: Add examples to show how to use the code.
1. **Document parameters and return values**: Clearly describe inputs and outputs.
1. **Set appropriate coverage thresholds**: Start with a reasonable threshold and gradually increase it.
1. **Run regularly**: Include Interrogate in your pre-commit hooks to maintain documentation quality.
1. **Add badges to README**: Display docstring coverage badges in your project README.

## Docstring Formats

Interrogate works with any docstring format, including:

=== "Google Style"
\`\`\`python linenums="1"
def function(param1, param2):
"""Summary line. # (1)

````
    Extended description.  # (2)

    Args:  # (3)
        param1: Description of param1
        param2: Description of param2

    Returns:  # (4)
        Description of return value
    """
    return result
```

1. Start with a concise summary
2. Add more details if needed
3. Document all parameters
4. Document return values
````

=== "NumPy Style"
\`\`\`python linenums="1"
def function(param1, param2):
"""
Summary line.

````
    Extended description.

    Parameters
    ----------
    param1 : type
        Description of param1
    param2 : type
        Description of param2

    Returns
    -------
    type
        Description of return value
    """
    return result
```
````

=== "reStructuredText Style"
\`\`\`python linenums="1"
def function(param1, param2):
"""Summary line.

````
    Extended description.

    :param param1: Description of param1
    :param param2: Description of param2
    :return: Description of return value
    """
    return result
```
````

## Resources

- [Interrogate Documentation](https://interrogate.readthedocs.io/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
