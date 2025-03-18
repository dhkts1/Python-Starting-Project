# Python Starting Project

A comprehensive learning template for Python applications with modern tools and best practices.

If you know uv ,git, and cursor/VSCODE, and have python 3.11+ installed, just run the 4 commands below:

```bash
uv sync
uv venv
pre-commit install
# to run prehooks locally
poe pre
```
## Quick Setup

### Prerequisites

- Python 3.11+ installed on your system
- Git installed on your system
- Basic command-line knowledge

### Step 1: Install UV Package Manager

UV is a blazing-fast Python package manager written in Rust.

#### For MacOS/Linux:
1. Install [Cursor](https://cursor.sh/) - AI-powered code editor
2. Install [UV](https://docs.astral.sh/uv/getting-started/installation/) - Modern Python package manager

Verify installation with:

```bash
uv --version
```

### Step 2: Set Up Your Project

You can either start from our template or clone the repository directly:

#### Option A: Use GitHub Template

1. Go to the [Python Starting Project](https://github.com/dhkts1/Python-Starting-Project)
2. Click the green "Use this template" button
3. Choose "Create a new repository"
4. Fill in your repository details
5. Clone your new repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

#### Option B: Direct Clone

```bash
git clone https://github.com/dhkts1/Python-Starting-Project
cd Python-Starting-Project
```

### Step 5: Install Dependencies and Create Virtual Environment

```bash
uv sync
```

### Step 6: Set Up Pre-commit Hooks (all the format, linting, testing, etc tools that will run automatically when you commit)

```bash
# Install pre-commit hooks
pre-commit install
```

### Step 7: Verify Your Setup

```bash
# Run all pre-commit checks
poe pre
```

### Step 8: Run the Sample Application

```bash
# Run the main script
python -m src.main
```

You're all set! Start developing with confidence.

> **⚠️ WARNING**: This template configures most tools at their maximum strictness level. It is designed for new projects where you want to follow strict standards from the beginning.

## Purpose

This project serves as both a starting template and a learning tool for Python development best practices:

- **Modern Python Tools**: Learn to use cutting-edge tools like Ruff, Pyright, and UV
- **Code Quality**: Experience best practices for linting, testing, and documentation
- **Project Structure**: Learn how to organize a Python project properly
- **CI/CD Integration**: See how automated workflows improve code quality

## Documentation

For detailed information and guides, check out the project documentation:

- **[Getting Started](docs/getting-started.md)**: Detailed setup and usage instructions
- **[Tutorial: Setup Your First Project](docs/tutorials/setup-your-first-project.md)**: Step-by-step tutorial
- **[Why](docs/index.md)**: The story behind this project
- **[Architecture](docs/architecture/index.md)**: Configuration, logging, and project structure
- **[Development](docs/development/index.md)**: Workflow, pre-commit hooks, and best practices
- **[API Reference](docs/api/index.md)**: Detailed code documentation

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
