# Poethepoet - Python Task Runner

Poethepoet (poe) is a task runner that allows you to define and run tasks in your Python project. It's similar to npm scripts for JavaScript projects, but designed specifically for Python.

## Overview

Poethepoet provides:

- A simple way to define project tasks
- Integration with pyproject.toml
- Support for task dependencies and sequences
- Command-line arguments for tasks
- Environment variable configuration
- Cross-platform compatibility

## Installation

Poethepoet is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install poethepoet
```

## How It's Used in This Project

In this project, Poethepoet is used to:

1. Define common development tasks
2. Run linters and formatters
3. Execute tests
4. Build documentation
5. Generate code
6. Provide a consistent interface for various tools

## Configuration in This Project

Poethepoet is configured in the `pyproject.toml` file under the `[tool.poe.tasks]` section:

```toml
[tool.poe.tasks]
flynt = "flynt --aggressive --fail-on-change --quiet src tests"
lint = { sequence = ["pyupgrade", "flynt", "pyright", "ruff", "ruff-format"] }
mkdocs = { cmd = "mkdocs build" }
mkdocs-serve = { cmd = "mkdocs serve" }
mkinit = { sequence = ["mkinit-src", "mkinit-tests"] }
mkinit-src = { cmd = "mkinit src --relative --lazy_loader_typed --black --recursive -w" }
mkinit-tests = { cmd = "mkinit tests --relative --lazy_loader_typed --black --recursive -w" }
pre = "pre-commit run --all-files --show-diff-on-failure --verbose"
pre-commit = "pre-commit run --all-files"
pyright = "pyright"
pyupgrade = "pyupgrade --py311-plus"
radon = "radon cc src --min C --total-average"
ruff = "ruff check"
ruff-format = "ruff format"
bandit = "bandit -c pyproject.toml -r src --exclude tests,.venv,.git"
interrogate = "interrogate -v src"
test-coverage = "pytest -xvs -n auto --cov=src --cov-report=xml --cov-fail-under=80 --ignore=tests"
vulture = "vulture src --min-confidence 80"
xenon = "xenon src"
```

## Basic Usage

### Running Tasks

To run a Poethepoet task:

```bash
# Run via uv
uv run poe task-name

# Run directly (if poethepoet is installed globally or in the env)
poe task-name
```

### Common Tasks

```bash
# Run linters
poe lint

# Run tests with coverage
poe test-coverage

# Build documentation
poe mkdocs

# Serve documentation locally
poe mkdocs-serve

# Run pre-commit hooks
poe pre-commit

# Generate __init__.py files
poe mkinit
```

## Task Types

Poethepoet supports several types of tasks:

### Simple Command Tasks

```toml
task-name = "command --with --options"
```

### Command Tasks with Options

```toml
task-name = { cmd = "command --with --options" }
```

### Sequence Tasks

```toml
task-name = { sequence = ["task1", "task2", "task3"] }
```

### Script Tasks

```toml
task-name = { script = "python_module:function_name" }
```

### Shell Tasks

```toml
task-name = { shell = "echo 'Running in a shell'" }
```

## Advanced Features

### Task Dependencies

You can define tasks that depend on other tasks:

```toml
lint = { sequence = ["pyupgrade", "flynt", "pyright", "ruff", "ruff-format"] }
```

### Task Arguments

You can pass arguments to tasks:

```bash
poe ruff src/specific_module.py
```

### Environment Variables

You can set environment variables for tasks:

```toml
task-name = { cmd = "command", env = { VAR1 = "value1", VAR2 = "value2" } }
```

## Best Practices

1. **Group related tasks**: Use sequence tasks to group related operations.
2. **Use descriptive task names**: Choose names that clearly indicate what the task does.
3. **Document tasks**: Include comments in your pyproject.toml to explain complex tasks.
4. **Prefer poe over direct commands**: Use poe tasks to provide a consistent interface.
5. **Use task dependencies**: Break complex tasks into smaller, reusable tasks.

## Troubleshooting

### Common Issues

#### Task Not Found

If you get a "task not found" error:

1. Check the spelling of the task name
2. Ensure the task is defined in pyproject.toml
3. Make sure you're running the command from the project root

#### Task Fails with Error

If a task fails with an error:

1. Check the error message for details
2. Run the command directly to see if it works outside of poe
3. Check for environment or path issues

#### Arguments Not Passed Correctly

If arguments aren't being passed correctly:

1. Try quoting the arguments
2. Use `--` to separate poe arguments from task arguments
3. Check if the task is defined to accept arguments

## Resources

- [Poethepoet Documentation](https://github.com/nat-n/poethepoet)
- [Python Project Configuration with pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
- [Task Runner Comparison](https://github.com/nat-n/poethepoet#comparison-to-similar-tools)
