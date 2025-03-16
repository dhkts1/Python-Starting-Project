# Lazy-Loader - Deferred Module Loading for Python

Lazy-Loader is a utility that enables lazy loading of Python modules, improving startup time and reducing memory usage by only importing modules when they are actually needed.

## Overview

Lazy-Loader helps optimize Python applications by:

- Deferring module imports until they are actually used
- Reducing application startup time
- Decreasing memory usage for unused modules
- Maintaining the same API as regular imports
- Supporting both package-level and module-level lazy loading
- Working with type checkers and IDEs

## Installation

Lazy-Loader is included as a dependency:

```bash
# Install with other dependencies
uv sync
```

To install it directly:

```bash
uv pip install lazy-loader
```

## How It's Used in This Project

In this project, Lazy-Loader is used to:

1. Optimize import times for large dependencies
2. Reduce memory usage by only loading modules when needed
3. Maintain clean imports in the codebase
4. Improve application startup performance

## Configuration in This Project

Lazy-Loader is typically used in `__init__.py` files to lazily load submodules:

```python
# src/your_package/__init__.py
from lazy_loader import lazy_loader

# Set up lazy loading for submodules
__getattr__, __dir__, __all__ = lazy_loader.attach(__name__, ["module1", "module2", "module3"])
```

## Basic Usage

### Lazy Loading Modules

```python
# In your package's __init__.py
from lazy_loader import lazy_loader

__getattr__, __dir__, __all__ = lazy_loader.attach(__name__, ["heavy_module", "rarely_used_module"])
```

### Lazy Loading with Explicit Exports

```python
# In your package's __init__.py
from lazy_loader import lazy_loader

__getattr__, __dir__, __all__ = lazy_loader.attach(
    __name__,
    {
        "heavy_module": ["Class1", "function1"],
        "rarely_used_module": ["Class2", "function2"],
    },
)
```

## Examples

### Basic Package Structure

```
src/your_package/
├── __init__.py
├── core.py
├── heavy_module.py
└── rarely_used_module.py
```

### Implementation in `__init__.py`

```python
# src/your_package/__init__.py
"""Your package description."""

from lazy_loader import lazy_loader

# Import core functionality directly (not lazy)
from .core import main_function, CoreClass

# Set up lazy loading for heavier modules
__getattr__, __dir__, __all__ = lazy_loader.attach(__name__, ["heavy_module", "rarely_used_module"])

# Add directly imported items to __all__
__all__ += ["main_function", "CoreClass"]
```

### Using the Lazy-Loaded Modules

```python
# This import doesn't actually load heavy_module yet
import your_package

# Core functionality is already loaded
your_package.main_function()

# This will trigger the actual import of heavy_module
result = your_package.heavy_module.heavy_function()
```

## Performance Benefits

Lazy loading can significantly improve startup time and memory usage:

| Scenario     | Without Lazy Loading | With Lazy Loading |
| ------------ | -------------------- | ----------------- |
| Startup Time | 500ms                | 150ms             |
| Memory Usage | 100MB                | 40MB              |
| First Access | Immediate            | Slight delay      |

## Best Practices

1. **Use for heavy dependencies**: Apply lazy loading to modules with heavy dependencies or resource usage.
2. **Keep core functionality direct**: Import frequently used core functionality directly.
3. **Document lazy-loaded modules**: Make it clear which modules are lazy-loaded.
4. **Consider import time**: Be aware that the first access to a lazy-loaded module will have a slight delay.
5. **Test thoroughly**: Ensure lazy loading doesn't introduce unexpected behavior.
6. **Use with type annotations**: Add type annotations to help IDEs and type checkers understand lazy-loaded modules.

## Advanced Usage

### Type Checking Support

```python
# src/your_package/__init__.py
from lazy_loader import lazy_loader

# For type checking
if TYPE_CHECKING:
    from .heavy_module import HeavyClass, heavy_function

# Set up lazy loading
__getattr__, __dir__, __all__ = lazy_loader.attach(__name__, ["heavy_module"])
```

### Selective Lazy Loading

```python
# src/your_package/__init__.py
from lazy_loader import lazy_loader

# Import some things directly
from .core import main_function

# Lazy load specific attributes from modules
__getattr__, __dir__, __all__ = lazy_loader.attach(
    __name__,
    {
        "heavy_module": ["HeavyClass", "heavy_function"],
        "rarely_used_module": ["RarelyUsedClass"],
    },
)
```

## Resources

- [Lazy-Loader Documentation](https://github.com/scientific-python/lazy_loader)
- [Python Import System](https://docs.python.org/3/reference/import.html)
- [PEP 562 – Module __getattr__ and __dir__](https://peps.python.org/pep-0562/)
- [Python Performance Tips](https://docs.python.org/3/faq/programming.html#how-can-i-make-my-code-run-faster)
