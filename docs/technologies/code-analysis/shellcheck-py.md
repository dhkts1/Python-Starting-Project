# Shellcheck-py - Shell Script Linter for Python

Shellcheck-py is a Python wrapper for ShellCheck, a static analysis tool for shell scripts that finds bugs, style issues, and suspicious constructs in your shell scripts.

## Overview

Shellcheck-py helps improve shell script quality by:

- Finding and fixing common shell script bugs
- Identifying potential security issues
- Suggesting style improvements
- Detecting portability issues between different shell types
- Providing clear explanations for each issue
- Integrating with Python projects and pre-commit hooks

## Installation

Shellcheck-py is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install shellcheck-py
```

## How It's Used in This Project

In this project, Shellcheck-py is used to:

1. Validate shell scripts in the repository
2. Ensure shell scripts follow best practices
3. Prevent common shell scripting bugs
4. Run as part of the pre-commit hooks and CI/CD pipeline

## Configuration in This Project

Shellcheck-py is configured in the `.pre-commit-config.yaml` file:

```yaml
  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.9.0.5
    hooks:
      - id: shellcheck
        args: [--severity=warning]
```

This configuration:

- Runs shellcheck on all shell scripts
- Reports issues with severity level "warning" or higher

## Basic Usage

### Running Shellcheck

To run Shellcheck on shell scripts:

```bash
# Run on a specific script
uv run shellcheck scripts/setup.sh

# Run on all shell scripts in a directory
uv run shellcheck scripts/*.sh
```

### Common Command-Line Options

```bash
# Specify shell dialect
uv run shellcheck --shell=bash scripts/setup.sh

# Set minimum severity level
uv run shellcheck --severity=warning scripts/setup.sh

# Include specific error codes
uv run shellcheck --include=SC2086,SC2046 scripts/setup.sh

# Exclude specific error codes
uv run shellcheck --exclude=SC2086,SC2046 scripts/setup.sh
```

## Examples

### Common Issues Detected

```bash
# Double quote to prevent globbing and word splitting
echo $variable  # Warning: SC2086

# Correct version
echo "$variable"

# Useless echo with cat
cat file.txt | grep pattern  # Warning: SC2002

# Correct version
grep pattern file.txt

# Command injection vulnerability
eval "command $user_input"  # Error: SC2048

# Correct version (still be careful with user input)
eval "command ${user_input@Q}"
```

## Severity Levels

Shellcheck uses different severity levels for issues:

1. **Error**: Severe issues that are likely to cause incorrect behavior
2. **Warning**: Issues that may cause problems in certain situations
3. **Info**: Suggestions for better practices
4. **Style**: Style recommendations

## Common Error Codes

| Code    | Description                                             |
| ------- | ------------------------------------------------------- |
| SC1000s | Shell parser issues                                     |
| SC2000s | Common shell script issues                              |
| SC2086  | Double quote to prevent globbing and word splitting     |
| SC2046  | Quote to prevent word splitting/globbing                |
| SC2164  | Use \`cd ...                                            |
| SC2016  | Single quotes don't expand variables                    |
| SC2034  | Variable appears unused                                 |
| SC2155  | Declare and assign separately for better error handling |
| SC3000s | Shell-specific issues (bash, dash, ksh)                 |

## Best Practices

1. **Fix all errors**: Address all error-level issues before committing.
2. **Review warnings**: Most warnings should be fixed unless there's a good reason not to.
3. **Use shellcheck directives**: Use `# shellcheck disable=SC2086` for intentional exceptions.
4. **Document exceptions**: When disabling checks, add a comment explaining why.
5. **Run regularly**: Include shellcheck in your pre-commit hooks.
6. **Learn from issues**: Use shellcheck as a learning tool to improve your shell scripting skills.

## Resources

- [Shellcheck Documentation](https://github.com/koalaman/shellcheck)
- [Shellcheck-py Repository](https://github.com/shellcheck-py/shellcheck-py)
- [Shell Scripting Best Practices](https://google.github.io/styleguide/shellguide.html)
- [Common Shell Script Issues](https://www.shellcheck.net/wiki/)
