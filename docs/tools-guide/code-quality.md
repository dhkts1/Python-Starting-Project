# Code Quality Tools Guide

**Est. time to complete:** 20 minutes

## What You'll Learn

- The purpose and benefits of code quality tools
- How to use the main code quality tools in this project
- When to use different tools for specific needs
- How to troubleshoot common issues

## Quick Reference

| Tool        | Primary Use          | When to Use       | Complexity | Command              |
| ----------- | -------------------- | ----------------- | ---------- | -------------------- |
| Ruff        | Linting & Formatting | Daily development | ★★☆        | `poe ruff`           |
| Pyright     | Type checking        | Daily development | ★★☆        | `poe pyright`        |
| Bandit      | Security scanning    | Pre-commit        | ★☆☆        | (Runs automatically) |
| Vulture     | Dead code detection  | Pre-commit        | ★☆☆        | (Runs automatically) |
| Interrogate | Docstring coverage   | Pre-commit        | ★☆☆        | (Runs automatically) |

## Understanding Code Quality

Code quality tools help you write better, more maintainable code by automatically checking for:

- Syntax errors and bugs
- Inconsistent formatting
- Security vulnerabilities
- Missing documentation
- Performance issues
- Type errors

These tools are configured to work together seamlessly in this project, ensuring that your code meets high-quality standards without requiring significant manual effort.

## Ruff: Your Primary Code Quality Tool

### What It Does

Ruff is an extremely fast Python linter and formatter written in Rust. It combines the functionality of many Python linting tools into a single package, including:

- **Linting**: Finds errors, bugs, stylistic issues, and suspicious code
- **Formatting**: Ensures consistent code style (similar to Black)
- **Import sorting**: Organizes imports (similar to isort)
- **Code fixing**: Automatically fixes many issues

### Basic Usage

```bash
# Check for linting issues
poe ruff

# Format your code
poe ruff-format

# Both check and format
poe ruff-all
```

### Common Patterns

#### 1. Running Ruff while coding

The best practice is to run Ruff regularly as you code, rather than waiting until you're ready to commit. This helps catch issues early.

```bash
# After making changes to a file
poe ruff-all
```

#### 2. Understanding error codes

Ruff uses error codes to indicate different types of issues:

- `E`, `F`: Error/Fatal (must fix)
- `W`: Warning (should fix)
- `I`: Import related
- `D`: Documentation related

Example error message:

```
src/main.py:10:1: F401 'os' imported but unused
```

This tells you:

- File: src/main.py
- Line 10, column 1
- Error code: F401
- Issue: You imported 'os' but never used it

#### A quick cheat sheet for common error codes:

| Code | Meaning                        | How to Fix                         |
| ---- | ------------------------------ | ---------------------------------- |
| E501 | Line too long                  | Break the line into multiple lines |
| F401 | Unused import                  | Remove the unused import           |
| W293 | Blank line contains whitespace | Remove trailing whitespace         |
| D103 | Missing docstring              | Add a docstring to the function    |

### Troubleshooting

**Problem**: Too many errors when first running Ruff
**Solution**: Focus on fixing one category at a time, starting with E and F errors

**Problem**: Ruff is changing formatting you prefer
**Solution**: Adjust settings in pyproject.toml under [tool.ruff.format]

## Pyright: Type Checking for Safer Code

### What It Does

Pyright is a static type checker that helps find type-related errors without running your code. It uses Python's type hints to:

- Catch type errors before runtime
- Improve code navigation and completion in your editor
- Document expected input and output types

### Basic Usage

```bash
# Run type checking on your project
poe pyright

# Specific file
pyright src/specific_file.py
```

### Simple Type Annotation Examples

```python
# Variables
name: str = "John"
age: int = 30

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Optional parameters
def process_data(data: list[str], debug: bool = False) -> dict[str, int]:
    # Process data
    return {"count": len(data)}
```

### Troubleshooting

**Problem**: "Cannot find module" errors
**Solution**: Make sure the module is installed and in your Python path

**Problem**: Too many "Unknown type" errors
**Solution**: Add type annotations gradually, focusing on function parameters and return types first

## Other Code Quality Tools

This project includes several other tools that run automatically as part of the pre-commit process:

### Bandit

Checks for security issues in your code, such as:

- Hardcoded passwords
- SQL injection vulnerabilities
- Use of insecure functions

### Vulture

Finds unused code that can be safely removed, including:

- Unused variables
- Unused functions and classes
- Unreachable code

### Interrogate

Checks docstring coverage to ensure your code is well-documented:

- Verifies functions have docstrings
- Monitors overall docstring coverage percentage
- Ensures documentation stays up-to-date with code

## Tool Comparison: When to Use What

| If You Need To...         | Use This Tool | Example Scenario                                  |
| ------------------------- | ------------- | ------------------------------------------------- |
| Fix syntax and style      | Ruff          | Ensuring consistent code style across the project |
| Catch type errors         | Pyright       | Validating function parameters and return types   |
| Check for security issues | Bandit        | Before deploying code that handles sensitive data |
| Clean up unused code      | Vulture       | When refactoring or maintaining legacy code       |
| Improve documentation     | Interrogate   | When preparing code for team contribution         |

## Practical Example: Fixing Common Issues

Let's say you have this code with several issues:

```python
import os
import sys

def calculate_result(input):
    if input > 10:
        print("Value is greater than 10")
        result = input * 2
    return result
```

Running our tools would find these issues:

1. `import os` is unused (Ruff F401)
2. Function is missing a docstring (Interrogate)
3. Parameter `input` has no type annotation (Pyright)
4. `result` might be undefined if input ≤ 10 (Pyright, Ruff)
5. Using print for logging is discouraged (Ruff)

Here's the corrected version:

```python
import sys
from logging import getLogger

logger = getLogger(__name__)

def calculate_result(input_value: int) -> int:
    """Calculate a result based on the input value.

    Args:
        input_value: The number to process

    Returns:
        The calculated result
    """
    result = 0
    if input_value > 10:
        logger.debug("Value is greater than 10")
        result = input_value * 2
    return result
```

## Further Reading

- [Detailed Ruff documentation](../technologies/code-quality/ruff.md)
- [Detailed Pyright documentation](../technologies/code-analysis/pyright.md)
- [Understanding pre-commit hooks](../development/pre-commit-hooks.md)

## Check Your Understanding

1. What tool would you use to automatically format your code?

    - Ruff

2. Which tool helps identify type-related errors without running the code?

    - Pyright

3. What's the command to check and fix linting issues?

    - `poe ruff`

4. Which tool checks for security vulnerabilities?

    - Bandit

5. What's the recommended frequency for running code quality tools?

    - Regularly while coding, before committing changes
