# Bandit - Security Linter for Python

Bandit is a security linter for Python code, designed to find common security issues and vulnerabilities in your codebase.

## Overview

Bandit scans Python code for common security issues such as:

- Hardcoded passwords and secrets
- SQL injection vulnerabilities
- Command injection vulnerabilities
- Insecure use of cryptographic functions
- Use of potentially dangerous functions
- Insecure file permissions
- And many other security concerns

It works by parsing the abstract syntax tree (AST) of Python files and running a series of plugins that look for specific patterns associated with security issues.

## Installation

Bandit is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install bandit
```

## How It's Used in This Project

In this project, Bandit is used to:

1. Identify potential security vulnerabilities in the codebase
2. Enforce security best practices
3. Prevent common security mistakes
4. Run as part of the pre-commit hooks and CI/CD pipeline

## Configuration in This Project

Bandit is configured in the `pyproject.toml` file:

```toml
[tool.bandit]
exclude_dirs = ["tests", ".venv", ".git"]
skips = ["B101"]                          # Skip assert statements warning
```

This configuration:

- Excludes test directories and virtual environments from scanning
- Skips the B101 check (use of assert statements), which is often a false positive in test code

Bandit is also configured as a poethepoet task:

```toml
[tool.poe.tasks]
bandit = "bandit -c pyproject.toml -r src --exclude tests,.venv,.git"
```

## Basic Usage

### Running Bandit

To run Bandit on the project:

```bash
# Run via poethepoet
uv run poe bandit

# Run directly
uv run bandit -c pyproject.toml -r src
```

### Common Command-Line Options

```bash
# Scan a specific file
uv run bandit path/to/file.py

# Scan a directory recursively
uv run bandit -r path/to/directory

# Specify severity level
uv run bandit -r src -l high

# Specify confidence level
uv run bandit -r src -c medium

# Generate a report
uv run bandit -r src -f json -o bandit-report.json
```

## Common Security Issues

### B101: Use of assert statements

```python
# Potentially problematic (assertions can be disabled with -O)
assert user.is_authenticated()

# Better approach
if not user.is_authenticated():
    raise PermissionError("User not authenticated")
```

### B102: Use of exec

```python
# Dangerous
exec(user_input)

# Better approach
# Avoid exec entirely, use safer alternatives
```

### B103: Setting permissive file permissions

```python
# Insecure
open("sensitive.txt", "w").write("secret")

# More secure
import os

with open("sensitive.txt", "w") as f:
    os.chmod("sensitive.txt", 0o600)  # Owner read/write only
    f.write("secret")
```

### B104-B107: Hardcoded passwords and secrets

```python
# Insecure
password = "hardcoded_password"

# Better approach
import os

password = os.environ.get("PASSWORD")
```

### B301-B315: Use of insecure functions

```python
# Insecure
import pickle

data = pickle.loads(user_input)  # Arbitrary code execution risk

# Better approach
import json

data = json.loads(user_input)
```

## Best Practices

1. **Run Bandit regularly**: Include Bandit in your pre-commit hooks and CI/CD pipeline.
2. **Address high-severity issues immediately**: High-severity issues with high confidence should be fixed as soon as possible.
3. **Review false positives**: Some issues flagged by Bandit may be false positives. Review them carefully and add skips only when necessary.
4. **Use context-specific configurations**: Different parts of your codebase may need different security checks.
5. **Keep Bandit updated**: Security tools should be kept up to date to catch the latest known vulnerabilities.

## Troubleshooting

### Common Issues

#### Too Many False Positives

If you're getting too many false positives:

1. Review the issues to ensure they're actually false positives
2. Add specific skips for the relevant checks in `pyproject.toml`
3. Use inline skips for specific lines: `# nosec` or `# nosec B101`

#### Integration with Other Tools

If you're having issues integrating Bandit with other tools:

1. Ensure you're using compatible versions
2. Check that your configuration files are correctly formatted
3. Try running Bandit directly to isolate the issue

## Resources

- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Bandit GitHub Repository](https://github.com/PyCQA/bandit)
- [OWASP Python Security Project](https://owasp.org/www-project-python-security/)
- [Common Security Issues in Python](https://snyk.io/blog/python-security-best-practices-cheat-sheet/)
