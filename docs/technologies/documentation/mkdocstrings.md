# MkDocstrings - API Documentation Generator

MkDocstrings is a powerful MkDocs plugin that automatically generates API documentation from your Python docstrings, enabling seamless integration of code documentation into your project's documentation site.

## Overview

MkDocstrings enhances your documentation by:

- Automatically generating API documentation from docstrings
- Supporting multiple docstring styles (Google, NumPy, reStructuredText)
- Providing cross-references between documentation pages
- Enabling customizable rendering of docstrings
- Supporting multiple programming languages (primarily Python)
- Integrating seamlessly with MkDocs and MkDocs Material
- Reducing documentation maintenance overhead

## Installation

MkDocstrings is included as a development dependency:

```bash linenums="1"
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash linenums="1"
uv pip install mkdocstrings[python]
```

## How It's Used in This Project

In this project, MkDocstrings is used to:

1. Generate comprehensive API documentation from Python docstrings
1. Maintain consistency between code and documentation
1. Provide detailed function, class, and module documentation
1. Reduce manual documentation effort
1. Ensure documentation stays up-to-date with code changes

## Configuration in This Project

MkDocstrings is configured in the `mkdocs.yml` file:

```yaml linenums="1"
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: true
            show_bases: true
            show_signature: true
            heading_level: 2
            docstring_style: google
            docstring_section_style: spacy
            members_order: source
            show_category_heading: true
            show_if_no_docstring: false
```

1. Enables the MkDocstrings plugin
1. Configures the Python handler
1. Shows source code in documentation
1. Uses Google-style docstrings

## Basic Usage

### Documenting Code

Write docstrings in your Python code:

```python linenums="1"
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.

    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be positive")
    return length * width
```

1. Function signature with type hints
1. Short description of the function
1. Documentation of parameters
1. Documentation of return value
1. Documentation of exceptions

### Referencing in Markdown

Reference your code in Markdown files:

```markdown linenums="1"
# API Reference

::: my_module.calculate_area
```

1. This directive tells MkDocstrings to generate documentation for the `calculate_area` function

## Docstring Styles

=== "Google Style (Default)"
\`\`\`python linenums="1"
def function(param1, param2):
"""Summary line.

````
    Extended description.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Raises:
        ValueError: If something goes wrong.
    """
```
````

=== "NumPy Style"
\`\`\`python linenums="1"
def function(param1, param2):
"""Summary line.

````
    Extended description.

    Parameters
    ----------
    param1 : type
        Description of param1.
    param2 : type
        Description of param2.

    Returns
    -------
    type
        Description of return value.

    Raises
    ------
    ValueError
        If something goes wrong.
    """
```
````

=== "reStructuredText Style"
\`\`\`python linenums="1"
def function(param1, param2):
"""Summary line.

````
    Extended description.

    :param param1: Description of param1.
    :type param1: type
    :param param2: Description of param2.
    :type param2: type
    :returns: Description of return value.
    :rtype: type
    :raises ValueError: If something goes wrong.
    """
```
````

## Advanced Features

### Cross-References

Link to other documented objects:

```markdown linenums="1"
See the [`calculate_area`][my_module.calculate_area] function for more details.
```

1. Creates a link to the documentation for the `calculate_area` function

### Custom Selection

Select specific members to document:

```markdown linenums="1"
::: my_module.MyClass
    selection:
      members:
        - method_a
        - method_b
```

1. Only documents the specified methods

### Customizing Display

Customize the rendering of documentation:

```markdown linenums="1"
::: my_module.MyClass
    options:
      show_source: false
      show_bases: false
      heading_level: 3
```

1. Overrides the global options for this specific class

## Best Practices

1. **Be consistent with docstring style**: Choose one style (Google, NumPy, or reStructuredText) and use it consistently.
1. **Document all public APIs**: Ensure all public functions, classes, and methods have docstrings.
1. **Include type hints**: Use type hints in your code to enhance documentation.
1. **Document parameters and return values**: Always document parameters, return values, and exceptions.
1. **Keep docstrings up-to-date**: Update docstrings when code changes.
1. **Use examples**: Include examples in docstrings for complex functions.
1. **Be concise but complete**: Provide enough information without being overly verbose.
1. **Use cross-references**: Link to related documentation when appropriate.

## Integration with Type Hints

MkDocstrings works well with type hints:

```python linenums="1"
from typing import List, Dict, Optional

def process_data(data: List[Dict[str, str]],
                 filter_key: Optional[str] = None) -> Dict[str, int]:
    """Process the input data.

    Args:
        data: A list of dictionaries to process.
        filter_key: Optional key to filter results.

    Returns:
        A dictionary with processed results.
    """
```

1. Import type annotations from the typing module
1. Parameter with complex type annotation
1. Optional parameter with default value and return type annotation

## Troubleshooting

### Common Issues

#### Missing Documentation

If documentation is not appearing:

1. Check that the import path is correct
1. Verify that the module is importable from where MkDocs is run
1. Ensure the docstrings are properly formatted

#### Formatting Issues

If docstrings aren't rendering correctly:

1. Check that the docstring style in the configuration matches your code
1. Verify indentation in docstrings
1. Ensure all sections are properly formatted

#### Import Errors

If you encounter import errors:

1. Make sure your package is installed in the environment where MkDocs runs
1. Check for circular imports
1. Consider using the `watch` option to monitor for changes

## Resources

- [MkDocstrings Documentation](https://mkdocstrings.github.io/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
