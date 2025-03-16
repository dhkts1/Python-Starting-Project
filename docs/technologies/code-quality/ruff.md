# Ruff - Fast Python Linter and Formatter

Ruff is an extremely fast Python linter and formatter, written in Rust. It combines the functionality of many Python linting and formatting tools into a single, high-performance package.

## Overview

Ruff provides:

- Linting capabilities similar to flake8, pylint, and many other linters
- Code formatting similar to black
- Import sorting similar to isort
- Automatic code fixes for many issues
- Extensible rule system with over 700 built-in rules
- Blazing fast performance (10-100x faster than other tools)

## Installation

Ruff is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install ruff
```

## How It's Used in This Project

In this project, Ruff is used for:

1. Linting Python code to catch errors and enforce style
2. Formatting code to maintain consistent style
3. Sorting imports
4. Automatically fixing common issues
5. Running as part of the pre-commit hooks and CI/CD pipeline

## Configuration in This Project

Ruff is configured in the `pyproject.toml` file:

```toml
[tool.ruff]
exclude = [
  ".bzr",
  ".direnv",
  ".eggs",
  ".git",
  ".git-rewrite",
  ".hg",
  ".ipynb_checkpoints",
  ".mypy_cache",
  ".nox",
  ".pants.d",
  ".pyenv",
  ".pytest_cache",
  ".pytype",
  ".ruff_cache",
  ".svn",
  ".tox",
  ".venv",
  ".vscode",
  "__pypackages__",
  "_build",
  "buck-out",
  "build",
  "dist",
  "node_modules",
  "site-packages",
  "venv",
  "__init__.py",
]

fix = true
line-length = 120
src = ["src"]
target-version = "py311"

[tool.ruff.format]
docstring-code-format = true
docstring-code-line-length = "dynamic"
indent-style = "space"
line-ending = "auto"
quote-style = "double"
skip-magic-trailing-comma = false

[tool.ruff.lint]
extend-ignore = [
  "E203",   # Not PEP8 compliant and black insert space around slice
  "E501",   # Line too long. Disable it to allow long lines of comments
  "D401",   # First line should be in imperative mood
  "D203",   # Removed incompatible rule (keep D211 instead)
  "D213",   # Removed incompatible rule (keep D212 instead)
  "COM812", # Removed rule that may conflict with formatter
  "F811",   # Redefined variable from import
  "ISC001",
  "BLE001",
  "PGH",
  "C901",   # Too complex
  "PLR",
  "TRY300",
]
extend-select = [
  "ALL",
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["D104"] # Allow __init__.py stuff
"tests/**/*.py" = [
  "S101",
  "ARG001",
  "FBT001",
] # Allow assert statements in tests, unused function arguments, and boolean positional arguments
```

Ruff is also configured as poethepoet tasks:

```toml
[tool.poe.tasks]
ruff = "ruff check"
ruff-format = "ruff format"
```

## Basic Usage

### Running Ruff Linter

To run Ruff linter on the project:

```bash
# Run via poethepoet
uv run poe ruff-check

# Run directly
uv run ruff check
```

### Running Ruff Formatter

To format code with Ruff:

```bash
# Run via poethepoet
uv run poe ruff-format

# Run directly
uv run ruff format
```

### Common Command-Line Options

```bash
# Check specific files or directories
uv run ruff check path/to/file.py

# Format specific files or directories
uv run ruff format path/to/file.py

# Fix issues automatically
uv run ruff check --fix

# Show error codes
uv run ruff check --show-fixes

# Select specific rule categories
uv run ruff check --select E,F,W

# Ignore specific rule categories
uv run ruff check --ignore E501,F401
```

## Understanding Ruff Rules

Ruff includes rules from many different linters, each with its own prefix:

- `E`, `F`, `W`: flake8 errors, fatal errors, and warnings
- `I`: isort import sorting
- `N`: pep8-naming
- `D`: pydocstyle
- `UP`: pyupgrade
- `B`: flake8-bugbear
- `C`: flake8-comprehensions
- `SIM`: flake8-simplify
- `ARG`: flake8-unused-arguments
- `PTH`: flake8-use-pathlib
- `ERA`: eradicate
- `PD`: pandas-vet
- `PL`: Pylint
- `TRY`: tryceratops
- `RUF`: Ruff-specific rules

And many more. See the [Ruff documentation](https://docs.astral.sh/ruff/rules/) for a complete list.

## Best Practices

1. **Run Ruff before committing**: Use pre-commit hooks to run Ruff automatically.
2. **Use `--fix` for automatic fixes**: Let Ruff fix simple issues automatically.
3. **Customize rules for your project**: Adjust the rule set to match your project's needs.
4. **Use per-file ignores for special cases**: Some files may need different rules.
5. **Keep configuration in pyproject.toml**: Centralize all tool configurations in one file.
6. **Update Ruff regularly**: Newer versions often include performance improvements and new rules.

## Troubleshooting

### Common Issues

#### Too Many Errors

If you're getting too many errors when first adding Ruff:

1. Start with a smaller rule set: `--select E,F,W`
2. Gradually add more rules as you fix issues
3. Use `--fix` to automatically fix simple issues
4. Add specific ignores for rules that don't apply to your project

#### Conflicts with Other Tools

If Ruff conflicts with other tools:

1. Consider replacing the other tools with Ruff
2. Adjust Ruff's configuration to match the other tools
3. Use per-file ignores to handle special cases

#### Performance Issues

If Ruff is running slowly (which is rare):

1. Exclude large directories that don't need linting
2. Use a more specific file selection
3. Update to the latest version of Ruff

## Resources

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Ruff Rules Reference](https://docs.astral.sh/ruff/rules/)
- [Ruff GitHub Repository](https://github.com/astral-sh/ruff)
- [Migrating from Other Linters](https://docs.astral.sh/ruff/migration/)
