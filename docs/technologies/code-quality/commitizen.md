# Commitizen - Standardized Commit Messages

Commitizen is a tool that helps standardize commit messages following the Conventional Commits specification, making your Git history more readable and useful.

## Overview

Commitizen provides a command-line interface that guides you through creating properly formatted commit messages. It helps:

- Enforce a consistent commit message format
- Generate changelogs automatically
- Simplify semantic versioning
- Improve collaboration through clear commit intentions
- Make Git history more readable and useful

## Installation

Commitizen is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install commitizen
```

## How It's Used in This Project

In this project, Commitizen is used to:

1. Standardize commit messages following the Conventional Commits specification
2. Enforce commit message format through pre-commit hooks
3. Facilitate automatic changelog generation
4. Support semantic versioning

## Configuration in This Project

Commitizen is configured in the `pyproject.toml` file:

```toml
[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
```

## Basic Usage

### Creating a Commit with Commitizen

Instead of using `git commit` directly, use:

```bash
# Interactive commit creation
uv run cz commit

# Or the shorter alias
uv run cz c
```

This will guide you through a series of prompts:

1. Select the type of change (feat, fix, docs, etc.)
2. Enter the scope (optional)
3. Write a short description
4. Provide a longer description (optional)
5. Indicate breaking changes (optional)
6. Reference issues (optional)

### Common Command-Line Options

```bash
# Commit with a message directly
uv run cz commit -m "feat: add new feature"

# Commit all changes
uv run cz commit -a

# Check if the last commit message follows the convention
uv run cz check --rev-range HEAD~1..HEAD
```

## Examples

### Conventional Commit Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Sample Commit Messages

```
feat(auth): add OAuth2 authentication

Implement OAuth2 authentication flow with Google and GitHub providers.

BREAKING CHANGE: The previous authentication system is no longer supported.
Refs: #123
```

```
fix(api): correct response status code for invalid requests

The API was returning 500 instead of 400 for invalid requests.
```

```
docs: update installation instructions

Update installation instructions to include the new uv package manager.
```

## Best Practices

1. **Be specific in your commit messages**: Clearly describe what changes were made and why.
2. **Use appropriate types**: Choose the correct type (feat, fix, docs, etc.) for your changes.
3. **Include scope when relevant**: Specify which part of the codebase was affected.
4. **Reference issues**: Link commits to related issues or pull requests.
5. **Keep descriptions concise**: Aim for 50-72 characters in the summary line.
6. **Use imperative mood**: Write "add feature" instead of "added feature" or "adds feature".

## Commit Types

| Type       | Description                                          |
| ---------- | ---------------------------------------------------- |
| `feat`     | A new feature                                        |
| `fix`      | A bug fix                                            |
| `docs`     | Documentation changes                                |
| `style`    | Code style changes (formatting, missing semi-colons) |
| `refactor` | Code changes that neither fix bugs nor add features  |
| `perf`     | Performance improvements                             |
| `test`     | Adding or correcting tests                           |
| `build`    | Changes to build system or dependencies              |
| `ci`       | Changes to CI configuration                          |
| `chore`    | Other changes that don't modify src or test files    |

## Resources

- [Commitizen Documentation](https://commitizen-tools.github.io/commitizen/)
- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
