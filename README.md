# Python Starting Project

A comprehensive learning template for Python applications with modern tools and best practices.

## Quick Setup

1. Install [Cursor](https://cursor.sh/) - AI-powered code editor
2. Install [UV](https://docs.astral.sh/uv/getting-started/installation/) - Modern Python package manager
3. Clone the repository:
    ```
    git clone https://github.com/yourusername/python-starting-project.git
    cd python-starting-project
    ```
4. Set up the environment:
    ```
    uv sync
    uv venv
    uv run pre-commit install
    ```
5. Run pre-commit checks:
    ```
    poe pre
    ```
    This command checks for errors that the linter might have missed and will be run by Cursor automatically when it finishes processing your code. if not tell it to.

You're all set! Start developing with confidence.

> **⚠️ WARNING**: This template configures most tools at their maximum strictness level. It is not recommended for existing projects as it will likely generate hundreds of thousands of errors. This is designed for new projects where you can follow strict standards from the beginning.

## Learning Python Best Practices

This project serves as both a starting template and a learning tool for Python development best practices:

- **Modern Python Tools**: Learn to use cutting-edge tools like Ruff, Pyright, and UV
- **Code Quality**: Experience best practices for linting, testing, and documentation
- **Project Structure**: Learn how to organize a Python project
- **CI/CD Integration**: See how automated workflows improve code quality

## Project Structure

```
python-starting-project/
├── src/                  # Main source code
│   ├── utils/            # Utility modules
│   │   ├── settings.py   # Application settings
│   │   └── logging.py    # Logging configuration
│   ├── __init__.py       # Package initialization with lazy loading
│   └── main.py           # Application entry point
├── tests/                # Test directory
├── docs/                 # Documentation files
├── .github/              # GitHub configuration
├── mkdocs.yml            # MkDocs configuration
├── pyproject.toml        # Project configuration
└── .pre-commit-config.yaml # Pre-commit hooks configuration
```

## Documentation

For detailed information and the full story behind this project, check out the documentation:

- **[Getting Started](docs/getting-started.md)**: Detailed setup and usage
- **[Why](docs/index.md)**: The story behind this project
- **[Architecture](docs/architecture/index.md)**: Configuration, logging, and project structure
- **[Development](docs/development/index.md)**: Workflow, pre-commit hooks, and best practices
- **[API Reference](docs/api/index.md)**: Detailed code documentation

## Simplified Workflow

This project has a minimal learning curve with just a few commands:

1. **Install dependencies**: `uv sync`
2. **Run pre-commit checks**: `poe pre`

## Technologies and Tools

This project integrates a comprehensive set of modern Python tools and libraries:

### Core Dependencies

- **pydantic-settings**: Configuration management with validation
- **lazy-loader**: Lazy loading of modules to improve import performance

### Development Environment

- **Cursor**: AI-powered VSCode with intelligent code completion and error detection
- **UV**: Modern, fast Python package manager
- **Hatchling**: Build backend for Python packages
- **poethepoet**: Task runner for Python projects

### Code Quality & Linting

- **Ruff**: Fast Python linter and formatter
- **Pyright**: Static type checker
- **Bandit**: Security vulnerability scanner
- **Vulture**: Dead code detector
- **Interrogate**: Docstring coverage checker
- **Darglint**: Docstring style checker
- **Xenon**: Code complexity monitor
- **Radon**: Code metrics tool
- **Codespell**: Spell checker for code
- **Flynt**: Converts string formatting to f-strings
- **PyUpgrade**: Upgrades Python syntax to newer versions
- **YesQA**: Removes unnecessary noqa comments

### Testing

- **Pytest**: Testing framework
- **Pytest-Cov**: Test coverage plugin
- **Pytest-AsyncIO**: Async testing support
- **Pytest-XDist**: Parallel test execution

### Documentation

- **MkDocs**: Documentation generator
- **MkDocs-Material**: Material theme for MkDocs
- **MkDocstrings**: API documentation from docstrings
- **MkDocs-Include-Markdown-Plugin**: Include markdown files in docs
- **MDFormat**: Markdown formatter with various extensions:
  - mdformat-config
  - mdformat-web
  - mdformat-tables
  - mdformat-frontmatter
  - mdformat-mkdocs
  - mdformat-gfm

### Project Management

- **MkInit**: Automatic `__init__.py` file generator
- **Pre-commit**: Git hooks framework
- **Commitizen**: Standardized commit messages
- **ShellCheck-py**: Shell script linter
- **Actionlint**: GitHub Actions workflow linter
- **Gitleaks**: Secret scanner for repositories
- **validate-pyproject**: Validates pyproject.toml file

### Additional Hooks

The pre-commit configuration includes additional hooks:
- Check YAML files
- Debug statements detection
- Trailing whitespace removal
- Mixed line ending fixing
- Built-in literals checking
- AST checking
- Merge conflict detection
- Shebang checking
- Docstring positioning
- Byte order marker fixing
- Case conflict checking
- TOML checking
- File contents sorting

Visit the [documentation](docs/technologies/index.md) for more details about these tools and technologies.

## Project Status

This project is actively maintained and monitored for code quality through various metrics:

<!-- mdformat-skip-start -->

### Code Quality
![Pre-commit](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B0%5D.message&label=pre-commit&logo=github&color=%24.badges%5B0%5D.color)
![Ruff](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B2%5D.message&label=ruff&logo=ruff&color=%24.badges%5B2%5D.color)
![Typing](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B3%5D.message&label=typing&logo=python&color=%24.badges%5B3%5D.color)
![Dead Code](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B4%5D.message&label=dead%20code&logo=python&color=%24.badges%5B4%5D.color)
![Security](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B5%5D.message&label=security&logo=shieldsdotio&color=%24.badges%5B5%5D.color)

### Testing & Documentation
![Coverage](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B1%5D.message&label=coverage&logo=pytest&color=%24.badges%5B1%5D.color)
![Docs](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B6%5D.message&label=docs&logo=readthedocs&color=%24.badges%5B6%5D.color)
![MkDocs](https://img.shields.io/badge/documentation-MkDocs-blue.svg?logo=markdown)

### Code Maintainability
![Complexity](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B7%5D.message&label=complexity&logo=codacy&color=%24.badges%5B7%5D.color)
![Maintainability](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B8%5D.message&label=maintainability&logo=codeclimate&color=%24.badges%5B8%5D.color)

### Tools
![Gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue?logo=git)
![UV](https://img.shields.io/badge/package%20manager-uv-blue?logo=python)

<!-- mdformat-skip-end -->

These badges are updated automatically by our CI/CD pipeline and reflect the current status of the project.
