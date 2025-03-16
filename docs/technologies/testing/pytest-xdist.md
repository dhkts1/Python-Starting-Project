# Pytest-xdist - Distributed Testing with Pytest

Pytest-xdist is a pytest plugin that allows you to run tests in parallel across multiple CPUs or even multiple machines, significantly reducing test execution time.

## Overview

Pytest-xdist helps speed up test execution by:

- Running tests in parallel across multiple CPU cores
- Distributing tests across multiple machines
- Supporting load-balanced and grouped test execution
- Providing options for test isolation
- Integrating seamlessly with pytest's existing features
- Offering flexible configuration options

## Installation

Pytest-xdist is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pytest-xdist
```

## How It's Used in This Project

In this project, Pytest-xdist is used to:

1. Speed up test execution by running tests in parallel
1. Ensure tests are properly isolated and don't interfere with each other
1. Optimize CI/CD pipeline performance
1. Reduce feedback time during development

## Configuration in This Project

Pytest-xdist is configured in the `pyproject.toml` file:

```toml
[tool.pytest.ini_options]
addopts = "-xvs"
```

The `-x` option enables parallel test execution.

## Basic Usage

### Running Tests in Parallel

```bash
# Run tests using all available CPU cores
uv run pytest -n auto

# Run tests using a specific number of workers
uv run pytest -n 4

# Run tests with load balancing
uv run pytest -n 4 --dist=loadfile
```

### Common Command-Line Options

```bash
# Run tests in parallel with verbose output
uv run pytest -n 4 -v

# Run tests with load balancing based on execution time
uv run pytest -n auto --dist=loadscope

# Run tests with load balancing based on test file
uv run pytest -n auto --dist=loadfile

# Run tests with load balancing based on test module
uv run pytest -n auto --dist=loadmodule
```

## Distribution Modes

Pytest-xdist supports different distribution modes:

1. **`--dist=load`** (default): Distributes tests to available workers as they finish their previous tests
1. **`--dist=loadscope`**: Groups tests by module and class, ensuring related tests run on the same worker
1. **`--dist=loadfile`**: Groups tests by file, ensuring all tests from a file run on the same worker
1. **`--dist=loadgroup`**: Groups tests by the `xdist_group` marker
1. **`--dist=each`**: Runs the entire test suite on each worker with different parameters

## Examples

### Basic Parallel Execution

```bash
# Run tests using all available CPU cores
$ uv run pytest -n auto
============================= test session starts ==============================
platform linux -- Python 3.11.0, pytest-7.3.1, pluggy-1.0.0
rootdir: /path/to/project
plugins: xdist-3.3.1, asyncio-0.21.0, cov-4.1.0
gw0 [250] / gw1 [250] / gw2 [250] / gw3 [250]
...
```

### Using Test Groups

```python
# In your test file
import pytest

@pytest.mark.xdist_group(name="database")
def test_database_connection():
    # Test database connection
    ...

@pytest.mark.xdist_group(name="api")
def test_api_endpoint():
    # Test API endpoint
    ...
```

```bash
# Run tests with group-based distribution
uv run pytest -n 4 --dist=loadgroup
```

## Best Practices

1. **Ensure test isolation**: Make sure tests don't depend on each other or shared state.
1. **Use appropriate distribution mode**: Choose the right `--dist` option based on your test dependencies.
1. **Consider test data**: Be careful with tests that access the same test data or database.
1. **Balance parallelism**: More workers isn't always better; find the optimal number for your system.
1. **Use markers for grouping**: Use `xdist_group` markers to control how tests are distributed.
1. **Monitor resource usage**: Watch CPU, memory, and I/O usage during parallel test execution.
1. **Combine with pytest-cov**: Use `--cov-append` when combining with coverage measurement.

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Tests interfering with each other | Use `--dist=loadscope` or `--dist=loadfile` to group related tests |
| Database conflicts | Use separate test databases or transactions for isolation |
| Inconsistent test failures | Add the `--reruns` option to retry flaky tests |
| High resource usage | Reduce the number of workers with `-n` option |
| Slow test initialization | Use session-scoped fixtures for expensive setup operations |

## Resources

- [Pytest-xdist Documentation](https://pytest-xdist.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Parallel Testing Best Practices](https://pytest-xdist.readthedocs.io/en/latest/how-to.html)
- [Test Isolation Strategies](https://docs.pytest.org/en/latest/how-to/fixtures.html#fixture-scopes)
