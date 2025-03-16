# Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to run a series of checks on your code before committing. These hooks help maintain code quality, security, and consistency across the project.

## Installation

Pre-commit hooks are installed automatically when you run:

```bash
uv sync
pre-commit install
```

## Local Environment Integration

This project is configured to use your local uv environment for running pre-commit hooks instead of creating separate virtual environments for each hook. This approach:

- Makes hooks run faster by avoiding environment creation overhead
- Ensures hooks use the same dependencies as your project
- Provides consistent behavior between manual runs and pre-commit hooks

The configuration uses:

- `default_language_version: python: system` to use your system Python
- `language: system` for local hooks
- `uv run` prefix for commands to ensure they use your uv environment

## Available Hooks

### Code Quality

#### Ruff

[Ruff](https://github.com/astral-sh/ruff) is a fast Python linter and formatter written in Rust.

- **Purpose**: Lints and formats Python code
- **Configuration**: Configured in `pyproject.toml` under `[tool.ruff]`
- **Command**: `poe ruff`

#### Vulture

[Vulture](https://github.com/jendrikseipp/vulture) finds unused code in Python programs.

- **Purpose**: Identifies dead code (unused functions, classes, variables)
- **Configuration**: Configured in `pyproject.toml` under `[tool.vulture]`
- **Command**: `poe vulture`
- **Badge**: [![Vulture is used to find dead code](https://img.shields.io/badge/vulture-finds%20dead%20code-lightgrey)](https://github.com/jendrikseipp/vulture)

#### Radon

[Radon](https://github.com/rubik/radon) analyzes code complexity.

- **Purpose**: Computes cyclomatic complexity to identify overly complex functions
- **Configuration**: Configured via command-line arguments in `.pre-commit-config.yaml`
- **Command**: `poe radon`

#### PyUpgrade

[PyUpgrade](https://github.com/asottile/pyupgrade) automatically upgrades Python syntax.

- **Purpose**: Updates Python syntax to use newer language features
- **Command**: `poe pyupgrade`

#### Flynt

[Flynt](https://github.com/ikamensh/flynt) converts old string formatting to f-strings.

- **Purpose**: Modernizes string formatting
- **Command**: `poe flynt`

### Documentation

#### Interrogate

[Interrogate](https://github.com/econchick/interrogate) checks docstring coverage.

- **Purpose**: Ensures code is properly documented
- **Configuration**: Configured in `pyproject.toml` under `[tool.interrogate]`
- **Command**: `poe interrogate`
- **Badge**: [![Documentation Coverage](https://interrogate.readthedocs.io/en/latest/_static/interrogate_badge.svg)](https://github.com/econchick/interrogate)

#### Darglint

[Darglint](https://github.com/terrencepreilly/darglint) checks that docstring arguments match function signatures.

- **Purpose**: Ensures docstrings accurately reflect function parameters and return values
- **Configuration**: Configured in `pyproject.toml` under `[tool.darglint]`
- **Command**: Not available as a direct command

#### MDFormat

[MDFormat](https://github.com/executablebooks/mdformat) formats Markdown files.

- **Purpose**: Ensures consistent Markdown formatting
- **Command**: Not available as a direct command

### Security

#### Bandit

[Bandit](https://github.com/PyCQA/bandit) is a security linter for Python code.

- **Purpose**: Finds common security issues in Python code
- **Configuration**: Configured in `pyproject.toml` under `[tool.bandit]`
- **Command**: `poe bandit`
- **Badge**: [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

#### Gitleaks

[Gitleaks](https://github.com/gitleaks/gitleaks) detects hardcoded secrets.

- **Purpose**: Prevents committing sensitive information
- **Command**: Not available as a direct command

### Infrastructure

#### Actionlint

[Actionlint](https://github.com/rhysd/actionlint) lints GitHub Actions workflows.

- **Purpose**: Validates GitHub Actions workflow files
- **Command**: Not available as a direct command

#### Shellcheck

[Shellcheck](https://github.com/koalaman/shellcheck) lints shell scripts.

- **Purpose**: Finds bugs in shell scripts
- **Command**: Not available as a direct command

#### Commitizen

[Commitizen](https://github.com/commitizen-tools/commitizen) enforces conventional commit message format.

- **Purpose**: Standardizes commit messages for better changelog generation
- **Configuration**: Configured in `pyproject.toml` under `[tool.commitizen]`
- **Command**: Not available as a direct command
- **Badge**: [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

#### MkInit

[MkInit](https://github.com/Erotemic/mkinit) generates `__init__.py` files.

- **Purpose**: Automatically creates `__init__.py` files with lazy loading
- **Command**: `poe mkinit`

## Running All Hooks

To run all pre-commit hooks on all files:

```bash
poe pre-commit
```

This command uses `uv` to ensure all hooks run in your project's environment with the correct dependencies. If you're not using `uv` or want to use the Poetry equivalent:

```bash
poe pre-commit
```

## Continuous Integration

This project uses GitHub Actions to run pre-commit hooks in CI/CD pipelines. The workflow is defined in `.github/workflows/pre-commit.yml` and:

1. Runs on every pull request and push to the main branch
2. Uses uv for dependency management following Astral's best practices
3. Installs all project dependencies
4. Runs all pre-commit hooks on all files

This ensures that all code meets quality standards before being merged. The workflow configuration:

```yaml
name: Pre-commit Checks

on:
  pull_request:
  push:
    branches: [main]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          cache-dependency-glob: pyproject.toml

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version-file: pyproject.toml

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Run pre-commit hooks
        run: poe pre-commit
```

## Skipping Hooks

In rare cases, you may need to skip pre-commit hooks:

```bash
git commit --no-verify -m "Your commit message"
```

However, this is discouraged and should only be used in exceptional circumstances.

## Adding New Hooks

To add a new pre-commit hook:

1. Add the hook configuration to `.pre-commit-config.yaml`
2. Add any necessary dependencies to `pyproject.toml` under `[dependency-groups.dev]`
3. Add any tool-specific configuration to `pyproject.toml`
4. Run `uv sync` to install the new dependencies
5. Run `pre-commit install` to update the hooks
