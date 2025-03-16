# Pytest - Python Testing Framework

Pytest is a powerful, flexible testing framework for Python that makes it easy to write simple and scalable test cases.

## Overview

Pytest provides:

- A simple, expressive syntax for writing tests
- Powerful fixture system for test setup and teardown
- Comprehensive assertion introspection
- Plugin architecture for extending functionality
- Parallel test execution
- Test discovery and collection

## Installation

Pytest and its plugins are included as development dependencies:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pytest pytest-cov pytest-asyncio pytest-xdist
```

## How It's Used in This Project

In this project, Pytest is used to:

1. Write and run unit tests
2. Measure code coverage
3. Test asynchronous code
4. Run tests in parallel
5. Generate coverage reports

## Configuration in This Project

Pytest is configured in the `pyproject.toml` file:

```toml
[tool.pytest.ini_options]
asyncio_default_fixture_loop_scope = "function"
python_classes = ["Test*"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
testpaths = ["tests"]
```

Pytest is also configured as a poethepoet task for running tests with coverage:

```toml
[tool.poe.tasks]
test-coverage = "pytest -xvs -n auto --cov=src --cov-report=xml --cov-fail-under=80 --ignore=tests"
```

## Basic Usage

### Running Tests

To run tests:

```bash
# Run all tests with coverage
uv run poe test-coverage

# Run all tests
uv run pytest

# Run specific tests
uv run pytest tests/unit/test_specific.py

# Run tests matching a pattern
uv run pytest -k "test_pattern"
```

### Common Command-Line Options

```bash
# Run tests verbosely
uv run pytest -v

# Show extra test summary info
uv run pytest -v

# Stop after first failure
uv run pytest -x

# Drop into debugger on failure
uv run pytest --pdb

# Run tests in parallel
uv run pytest -n auto

# Measure code coverage
uv run pytest --cov=src
```

## Writing Tests

### Basic Test Structure

```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2


def test_string_methods():
    assert "hello".capitalize() == "Hello"
```

### Test Classes

```python
# test_example.py
class TestMathFunctions:
    def test_addition(self):
        assert 1 + 1 == 2

    def test_multiplication(self):
        assert 2 * 3 == 6
```

### Using Fixtures

```python
# test_example.py
import pytest


@pytest.fixture
def sample_data():
    return {"name": "Test User", "age": 30}


def test_user_name(sample_data):
    assert sample_data["name"] == "Test User"


def test_user_age(sample_data):
    assert sample_data["age"] == 30
```

### Testing Exceptions

```python
# test_example.py
import pytest


def divide(a, b):
    return a / b


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

### Parameterized Tests

```python
# test_example.py
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        (1, 1),
        (2, 4),
        (3, 9),
        (4, 16),
    ],
)
def test_square(input, expected):
    assert input**2 == expected
```

### Async Tests

```python
# test_example.py
import pytest


@pytest.mark.asyncio
async def test_async_function():
    result = await some_async_function()
    assert result == expected_value
```

## Plugins Used in This Project

### pytest-cov

Measures code coverage and generates reports:

```bash
uv run pytest --cov=src --cov-report=xml
```

### pytest-asyncio

Enables testing of asynchronous code:

```python
@pytest.mark.asyncio
async def test_async_function():
    # Test async code
```

### pytest-xdist

Enables parallel test execution:

```bash
uv run pytest -n auto  # Use all available CPU cores
uv run pytest -n 4     # Use 4 CPU cores
```

## Best Practices

1. **Follow naming conventions**: Name test files with `test_` prefix and test functions with `test_` prefix.
2. **Use fixtures for setup and teardown**: Avoid duplicating setup code across tests.
3. **Keep tests independent**: Tests should not depend on the state from other tests.
4. **Test one thing per test**: Each test should verify a single behavior.
5. **Use parameterized tests**: Test multiple inputs with a single test function.
6. **Aim for high coverage**: Strive for at least 80% code coverage.
7. **Include both positive and negative tests**: Test both expected and error cases.

## Troubleshooting

### Common Issues

#### Tests Not Being Discovered

If tests aren't being discovered:

1. Check that test files start with `test_`
2. Check that test functions start with `test_`
3. Check that test classes start with `Test`
4. Check the `testpaths` configuration

#### Fixture Errors

If you're having issues with fixtures:

1. Check fixture scope (function, class, module, session)
2. Check for circular dependencies between fixtures
3. Ensure fixtures are accessible to the tests that need them

#### Coverage Issues

If you're having issues with coverage:

1. Check that the source paths are correct
2. Ensure you're not excluding relevant files
3. Check for `.coveragerc` or configuration in `pyproject.toml`

## Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Pytest-asyncio Documentation](https://pytest-asyncio.readthedocs.io/)
- [Pytest-xdist Documentation](https://github.com/pytest-dev/pytest-xdist)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)
