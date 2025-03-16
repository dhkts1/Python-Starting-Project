# Pre-commit - Git Hooks Framework

Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks that run automatically before each git commit, ensuring code quality and consistency.

## Overview

Pre-commit helps maintain code quality by:

- Running code quality checks before each commit
- Supporting hooks for multiple languages and tools
- Preventing commits that don't meet quality standards
- Automating code formatting and linting
- Ensuring consistent code style across the project
- Integrating with CI/CD pipelines
- Supporting custom hooks for project-specific checks

## Installation

Pre-commit is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pre-commit
```

After installation, you need to install the git hooks:

```bash
uv run pre-commit install
```

## How It's Used in This Project

In this project, Pre-commit is used to:

1. Run code quality checks before each commit
2. Enforce consistent code style and formatting
3. Catch common issues early in the development process
4. Ensure documentation is properly formatted
5. Run security checks on the codebase

## Configuration in This Project

Pre-commit is configured in the `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [pydantic, types-requests]

  # Additional hooks...
```

## Basic Usage

### Running Pre-commit

```bash
# Run pre-commit on all files
uv run pre-commit run --all-files

# Run pre-commit on staged files
uv run pre-commit run

# Run a specific hook
uv run pre-commit run ruff --all-files
```

### Common Command-Line Options

```bash
# Skip specific hooks
uv run pre-commit run --all-files --hook-stage commit --skip ruff

# Run hooks on specific files
uv run pre-commit run --files src/module.py tests/test_module.py

# Show hook output even if successful
uv run pre-commit run --verbose
```

## Examples

### Pre-commit Output

```bash
$ uv run pre-commit run --all-files
Ruff............................................................Passed
Ruff Format....................................................Passed
mypy...........................................................Passed
Bandit.........................................................Passed
Vulture........................................................Passed
Pyright........................................................Passed
```

### Failed Check Example

```bash
$ uv run pre-commit run --all-files
Ruff............................................................Failed
- hook id: ruff
- exit code: 1

src/module.py:10:1: F401 [*] `os` imported but unused
src/module.py:25:5: E501 Line too long (88 > 79 characters)
```

## Hook Types

Pre-commit supports different types of hooks:

1. **pre-commit**: Runs before committing
2. **pre-push**: Runs before pushing
3. **pre-merge-commit**: Runs before merge commits
4. **pre-rebase**: Runs before rebasing
5. **commit-msg**: Runs to validate commit messages
6. **prepare-commit-msg**: Runs to prepare commit messages

## Best Practices

1. **Run hooks on all files periodically**: Use `pre-commit run --all-files` to check the entire codebase.
2. **Keep hooks fast**: Ensure hooks run quickly to avoid disrupting the development workflow.
3. **Use auto-fixing hooks**: Prefer hooks that can automatically fix issues when possible.
4. **Update hooks regularly**: Keep hook versions updated to benefit from improvements and bug fixes.
5. **Include pre-commit in CI**: Run pre-commit in CI to ensure all contributors follow the same standards.
6. **Document custom hooks**: If you add custom hooks, document their purpose and requirements.
7. **Use local hooks for project-specific checks**: Add local hooks for checks specific to your project.

## Common Hooks

| Hook           | Purpose                        |
| -------------- | ------------------------------ |
| `ruff`         | Python linter and formatter    |
| `mypy`         | Static type checking           |
| `black`        | Python code formatter          |
| `isort`        | Import sorter                  |
| `flake8`       | Python style guide enforcement |
| `bandit`       | Security linter                |
| `prettier`     | Multi-language formatter       |
| `markdownlint` | Markdown linter                |
| `shellcheck`   | Shell script linter            |

## Troubleshooting

### Skipping Hooks

To skip hooks for a specific commit:

```bash
git commit --no-verify -m "Your commit message"
```

### Updating Hooks

To update hooks to their latest versions:

```bash
uv run pre-commit autoupdate
```

### Clearing Cache

If you encounter issues with cached results or pyi files:

```bash
uv run pre-commit clean
poe mkinit
```

## Resources

- [Pre-commit Documentation](https://pre-commit.com/)
- [Available Hooks](https://pre-commit.com/hooks.html)
- [Git Hooks Documentation](https://git-scm.com/docs/githooks)
- [Creating Custom Hooks](https://pre-commit.com/#new-hooks)
