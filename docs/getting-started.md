# Python Starting Project

A comprehensive Python project template with built-in logging, configuration management, and development tools. This template provides a solid foundation for building Python applications with best practices for configuration, logging, code quality, and project structure.

<!-- Dynamic Badges -->

<!-- mdformat-skip-start -->

![Pre-commit](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B0%5D.message&label=pre-commit&color=red&logo=github)
![Coverage](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B1%5D.message&label=coverage&color=red&logo=pytest)
![Ruff](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B2%5D.message&label=ruff&color=green&logo=ruff)
![Typing](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B3%5D.message&label=typing&color=green&logo=python)
![Dead Code](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B4%5D.message&label=dead%20code&color=green&logo=python)
![Security](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B5%5D.message&label=security&color=green&logo=shieldsdotio)
![Documentation](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B7%5D.message&label=docs&color=green&logo=readthedocs)
![Complexity](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B8%5D.message&label=complexity&color=green&logo=codacy)
![Maintainability](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B9%5D.message&label=maintainability&color=green&logo=codeclimate)
![MkDocs](https://img.shields.io/badge/documentation-MkDocs-blue.svg?logo=markdown)

<!-- mdformat-skip-end -->

## Features

- **Structured project layout** with src-based architecture
- **Logging configuration** with console and file output
- **Settings management** using pydantic-settings
- **Environment variable support** with .env file override capability
- **Lazy loading** for improved import performance
- **Comprehensive testing** with pytest
- **Code quality tools**:
    - Ruff for linting and formatting
    - Pyright for static type checking
    - Bandit for security checks
    - Vulture for dead code detection
    - Interrogate for docstring coverage
    - Darglint for docstring validation
- **GitHub Actions** for CI/CD with pre-commit checks
- **Comprehensive badge system** with dynamic quality indicators
- **Documentation** with MkDocs for beautiful, searchable documentation

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management (recommended)
- An IDE: either [Visual Studio Code](https://code.visualstudio.com/) or [Cursor](https://cursor.sh) (recommended for AI-assisted development)

## Installation

### Important: Do not skip these steps!

```bash
# Clone the repository
git clone https://github.com/yourusername/python-starting-project.git
cd python-starting-project

# Install dependencies
uv sync

# Install pre-commit hooks:
uv run pre-commit install

# Run pre-commit hooks to verify everything works:
uv run poe pre
```

## Project Structure

The project follows a modular architecture with clear separation of concerns:

```
python-starting-project/
├── src/                  # Main source code
│   ├── utils/            # Utility modules
│   │   ├── settings.py   # Application settings
│   │   └── logging.py    # Logging configuration
│   ├── __init__.py       # Package initialization with lazy loading
│   └── main.py           # Application entry point
├── tests/                # Test directory
│   ├── unit/             # Unit tests
│   └── conftest.py       # Pytest configuration
├── docs/                 # Documentation files
│   ├── api/              # API reference documentation
│   ├── architecture/     # Architecture documentation
│   └── development/      # Development guides
├── .github/              # GitHub configuration
│   └── workflows/        # GitHub Actions workflows
│       └── ci.yml        # CI workflow with dynamic badges
├── .vscode/              # Editor configuration
├── mkdocs.yml            # MkDocs configuration
├── pyproject.toml        # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks configuration
└── .env.example          # Example environment configuration
```

## Simplified Workflow

This project is designed to have a minimal learning curve. You only need to know **4 commands** for the entire development cycle:

### 1. `uv sync`

This command installs or updates all project dependencies:

```bash
uv sync
```

**When to use it:**

- When you first clone the repository
- When dependencies are updated in `pyproject.toml`
- When switching to a branch with different dependencies

### 2. `uv run pre-commit install`

This command sets up the pre-commit hooks that automatically check your code quality before each commit:

```bash
uv run pre-commit install
```

**When to use it:**

- Only once after cloning the repository
- If you need to reinstall the pre-commit hooks

### 3. `git add`

This command stages your changes for commit:

```bash
# Add specific files
git add filename.py

# Add all changes
git add .
```

**When to use it:**

- After making changes you want to commit

### 4. `git commit`

This command commits your staged changes:

```bash
git commit -m "Your commit message"
```

**When to use it:**

- After staging your changes with `git add`
- The pre-commit hooks will automatically run before the commit is created
- If any hooks fail, the commit will be aborted until you fix the issues

### Complete Workflow Example

```bash
# Initial setup (only once)
uv sync
uv run pre-commit install

# Development cycle (repeat as needed)
# 1. Make changes to your code
# 2. Stage changes
git add .
# 3. Commit changes (pre-commit hooks run automatically)
git commit -m "Add new feature"
```

That's it! With just these 4 commands, you can handle the entire development workflow while maintaining high code quality standards.

## IDE Integration

The project is configured to work with both VSCode and Cursor:

### VSCode Integration

For the best development experience with VSCode:

1. Open the project in VSCode
2. Install recommended extensions when prompted
3. Use the integrated terminal for running commands
4. Use the built-in debugger for debugging

### Cursor Integration

Cursor provides all VSCode features plus AI-assisted development:

1. Open the project in Cursor
2. Cursor will automatically use the project's settings and extensions
3. Use AI features to help with code completion, refactoring, and documentation

## Next Steps

- Explore the [Architecture](architecture/configuration.md) documentation
- Learn about [Pre-commit Hooks](development/pre-commit-hooks.md)
- Check out the [API Reference](api/index.md)
