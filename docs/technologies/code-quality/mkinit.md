# Mkinit - Python `__init__.py` Generator

Mkinit is a tool that automatically generates or updates `__init__.py` files for Python packages, making imports cleaner and more maintainable.

## Overview

Mkinit scans Python modules in a package and automatically generates appropriate import statements for the `__init__.py` file. This helps:

- Maintain consistent and up-to-date package exports
- Reduce manual work when adding new modules to a package
- Ensure proper package structure and imports
- Simplify import statements for users of your package

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

In this project, Mkinit is used to:

1. Automatically generate and update `__init__.py` files
2. Ensure consistent package exports
3. Simplify the package structure for users
4. Run as part of the development workflow

## Configuration in This Project

Mkinit is configured as a poethepoet task:

```toml
[tool.poe.tasks]
mkinit = "mkinit"
```

## Basic Usage

### Running Mkinit

To run Mkinit on the project:

```bash
# Run via poethepoet
uv run poe mkinit

# Run directly on a specific package
uv run mkinit src/your_package
```

### Common Command-Line Options

```bash
# Generate __init__.py with explicit imports
uv run mkinit --nomodo src/your_package

# Generate __init__.py with __all__ statements
uv run mkinit --all src/your_package

# Specify a custom pattern for modules to include
uv run mkinit --pattern="*.py" src/your_package

# Dry run (show what would be generated without writing files)
uv run mkinit --dry src/your_package
```

## Examples

### Generated `__init__.py` File

For a package structure like:

```
src/your_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

Mkinit might generate an `__init__.py` like:

```python
# -*- coding: utf-8 -*-
"""
Package: your_package
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from your_package import subpackage
from your_package.module1 import Function1, Class1
from your_package.module2 import Function2, Class2

__all__ = ["subpackage", "Function1", "Class1", "Function2", "Class2"]
```

### Using Static Imports

You can also use Mkinit with static imports:

```python
# -*- coding: utf-8 -*-
"""
Package: your_package
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# <AUTOGEN_INIT>
from your_package import subpackage
from your_package.module1 import Function1, Class1
from your_package.module2 import Function2, Class2
# </AUTOGEN_INIT>
```

## Best Practices

1. **Run Mkinit after adding new modules**: Update your `__init__.py` files whenever you add new modules or classes.
2. **Use with version control**: Always commit the generated `__init__.py` files to your repository.
3. **Consider explicit imports**: For better IDE support, use explicit imports rather than wildcard imports.
4. **Add custom imports**: You can add custom imports outside the autogenerated section.
5. **Document your package structure**: Use the generated `__init__.py` files as a reference for your package structure.

## Resources

- [Mkinit Documentation](https://github.com/Erotemic/mkinit)
- [Python Packaging Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Import System in Python](https://docs.python.org/3/reference/import.html)
