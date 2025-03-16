# Python Starting Project

Welcome to the Python Starting Project documentation! This project provides a comprehensive template for Python applications with built-in logging, configuration management, and development tools.

<!-- Dynamic Badges -->

<!-- mdformat-skip-start -->

![Pre-commit](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B0%5D.message&label=pre-commit&logo=github&color=%24.badges%5B0%5D.color)
![Coverage](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B1%5D.message&label=coverage&logo=pytest&color=%24.badges%5B1%5D.color)
![Ruff](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B2%5D.message&label=ruff&logo=ruff&color=%24.badges%5B2%5D.color)
![Typing](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B3%5D.message&label=typing&logo=python&color=%24.badges%5B3%5D.color)
![Dead Code](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B4%5D.message&label=dead%20code&logo=python&color=%24.badges%5B4%5D.color)
![Security](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B5%5D.message&label=security&logo=shieldsdotio&color=%24.badges%5B5%5D.color)
![Docs](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B6%5D.message&label=docs&logo=readthedocs&color=%24.badges%5B6%5D.color)
![Complexity](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B7%5D.message&label=complexity&logo=codacy&color=%24.badges%5B7%5D.color)
![Maintainability](https://img.shields.io/badge/dynamic/json?url=https://gist.githubusercontent.com/dhkts1/ffa9b5234248225d681ef8ac4fe0a7e1/raw/badges.json&query=%24.badges%5B8%5D.message&label=maintainability&logo=codeclimate&color=%24.badges%5B8%5D.color)
![MkDocs](https://img.shields.io/badge/documentation-MkDocs-blue.svg?logo=markdown)
![Gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue?logo=git)
![UV](https://img.shields.io/badge/package%20manager-uv-blue?logo=python)

<!-- mdformat-skip-end -->

## TL;DR: Quick Setup

1. Install uv: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repository:
    ```
    git clone https://github.com/yourusername/python-starting-project.git
    cd python-starting-project
    ```
3. Set up the environment:
    ```
    uv sync
    uv venv
    uv run pre-commit install
    ```
4. Run pre-commit checks:
    ```
    poe pre
    ```
    This command checks for errors that the linter might have missed and will be run by Cursor automatically when it finishes processing your code.

You're all set! Start developing with confidence.

> **⚠️ WARNING**: This template configures most tools at their maximum strictness level. It is **STRONGLY NOT RECOMMENDED** to apply this configuration to existing projects, as it will likely generate hundreds of errors. This template is designed for new projects where you can follow the strict standards from the beginning. If you attempt to apply it to an existing project, may the code gods be with you.
>
> Despite the strict configuration, VSCode performance remains fast - probably faster than any setup you've ever seen. There's some magic under the hood that keeps things snappy. The first install might take some time, but the CI is fast, and in daily development you'll mostly use Ruff + Pyright + a few static extensions. If you find any extensions slowing you down, you can always disable them.
>
> This project uses the most bleeding-edge Python tools that are stable enough for production. Tools like Cursor (AI-powered VSCode), UV, Ruff, mkdocs, mkdocstrings, pyright, pyupgrade, flynt, bandit, vulture, interrogate, xenon, and many more represent the latest advancements in the Python ecosystem, offering significant performance improvements over traditional tools.

## Project Overview

This project provides a solid foundation for Python applications with best practices for configuration, logging, code quality, and project structure. It's designed to eliminate the setup pain and let you dive straight into development.

### Key Features

- **Minimal Setup**: Just a few commands to get started
- **Code Quality Tools**: Pre-configured linting, formatting, and type checking
- **Comprehensive Testing**: Built-in test framework with coverage reporting
- **Documentation**: Automatic documentation generation with MkDocs
- **CI/CD Integration**: GitHub Actions workflow with dynamic badges

### Tools Included

- **Ruff**: Fast Python linter and formatter
- **Pyright**: Static type checking
- **UV**: Modern Python package manager
- **Pytest**: Testing framework with coverage reporting
- **Bandit**: Security scanning
- **Vulture**: Dead code detection
- **MkDocs**: Documentation generator
- **Pre-commit**: Git hooks for code quality

### Project Structure

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

## Simplified Workflow

This project is designed to have a minimal learning curve. You only need to know a few commands for the entire development cycle:

1. **Install dependencies**: `uv sync`
2. **Set up pre-commit hooks**: `uv run pre-commit install` (once after cloning)
3. **Run pre-commit checks**: `poe pre`

## Documentation

For more detailed information, check out the documentation:

- **Getting Started**: Basic setup and usage
- **Architecture**: Configuration, logging, and project structure
- **Development**: Workflow, pre-commit hooks, and best practices
- **API Reference**: Detailed documentation of the codebase

## Why This Project?

Setting up a new Python project with all the best practices and tools can be time-consuming. This template solves that problem by providing a pre-configured environment that:

- Enforces code quality through automated checks
- Provides comprehensive documentation
- Integrates modern Python tools
- Follows best practices for project structure

Whether you're starting a new project or looking to improve your development workflow, this template gives you a solid foundation to build upon.

## Technologies and Packages

### Core Dependencies

- **pydantic-settings**: Configuration management with validation
- **lazy-loader**: Lazy loading of modules to improve import performance

### Package Management

- **UV**: Modern, fast Python package manager
- **Hatchling**: Build backend for Python packages

### Code Quality & Linting

- **Cursor**: AI-powered VSCode that enhances productivity with intelligent code completion, refactoring, and error detection
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
- **MDFormat**: Markdown formatter

### Project Structure

- **MkInit**: Automatic __init__.py file generator
- **Lazy-Loader**: Lazy import mechanism for Python modules

### Task Running

- **Poethepoet**: Task runner for Python projects

### Version Control & CI

- **Pre-commit**: Git hooks framework
- **Commitizen**: Standardized commit messages
- **ShellCheck-py**: Shell script linter
- **Actionlint**: GitHub Actions workflow linter
- **Gitleaks**: Secret scanner for repositories

### Dynamic Badges

This project includes a GitHub Actions workflow that generates dynamic badges for code quality metrics:

- **Pre-commit**: Shows if all pre-commit hooks pass
- **Coverage**: Displays test coverage percentage
- **Ruff**: Indicates if code passes Ruff linting
- **Typing**: Shows Pyright type checking status
- **Dead Code**: Reports Vulture dead code detection results
- **Security**: Shows Bandit security check status
- **Documentation**: Displays Interrogate docstring coverage
- **Complexity**: Shows Radon code complexity rating
- **Maintainability**: Indicates Xenon code maintainability status

#### Setting Up Badges

To enable the dynamic badges:

1. Create a GitHub Gist to store the badge data:

    - Go to https://gist.github.com/ and create a new gist
    - Create a file named `badges.json` (content doesn't matter, it will be overwritten)
    - Make sure the Gist is **public** so the badge images can be accessed without authentication
    - Note the Gist ID from the URL (the alphanumeric string after your username)

2. Create a Personal Access Token (PAT) with `gist` scope:

    - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
    - Generate a new token with the `gist` scope
    - Copy the generated token

3. Add the following secrets to your repository:

    - Go to your repository → Settings → Secrets and variables → Actions
    - Add `BADGES_GIST_ID` with your Gist ID value
    - Add `BADGES_TOKEN` with your Personal Access Token

4. Enable badges in your repository:

    - Go to your repository → Settings → Secrets and variables → Actions
    - Under "Variables", add `ENABLE_BADGES` with value `true`

5. Update the badge URLs in your README.md:

    - Replace the URL in the badge markdown with your Gist URL
    - Example: `![Badge](https://img.shields.io/dynamic/json?url=https://gist.githubusercontent.com/YOUR_USERNAME/YOUR_GIST_ID/raw/badges.json&query=$.badges[?(@.label%3D%3D%27pre-commit%27)].message&label=pre-commit&color=green)`

The badges workflow is disabled by default to avoid unnecessary GitHub Actions usage. It will only run when the `ENABLE_BADGES` repository variable is set to `true`.

#### Dependabot Integration

For Dependabot to work with the badges workflow, additional configuration has been added:

1. The `.github/dependabot.yml` file includes permissions for Dependabot to access the badge secrets.

### Other Tools

- **validate-pyproject**: Validates pyproject.toml file
- Various pre-commit hooks for code quality

### AI & Agents

- **Model Context Protocol (MCP)**: Framework for building AI agents that can perform complex tasks
- **Sequential Thinking**: MCP agent for step-by-step problem solving
- **Fetch**: MCP agent for retrieving information from the web
