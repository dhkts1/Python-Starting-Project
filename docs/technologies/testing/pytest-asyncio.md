# Pytest-asyncio - Testing Asynchronous Code with Pytest

Pytest-asyncio is a pytest plugin that provides support for testing asynchronous code based on asyncio, Python's standard library for writing concurrent code using the async/await syntax.

## Overview

Pytest-asyncio helps test asynchronous code by:

- Providing fixtures for testing asyncio coroutines
- Managing the asyncio event loop during tests
- Supporting both function and class-based async tests
- Handling test teardown properly for async resources
- Integrating seamlessly with pytest's existing features
- Supporting Python 3.7+ asyncio features

## Installation

Pytest-asyncio is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pytest-asyncio
```

## How It's Used in This Project

In this project, Pytest-asyncio is used to:

1. Test asynchronous functions and coroutines
2. Ensure proper handling of async resources
3. Validate async API behavior
4. Test concurrent operations

## Configuration in This Project

Pytest-asyncio is configured in the `pyproject.toml` file:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

This configuration enables automatic detection of async tests, which means:

- Tests defined with `async def` are automatically treated as asyncio tests
- The event loop is automatically created and managed for each test

## Basic Usage

### Writing Asynchronous Tests

```python
# Simple async test
async def test_async_function():
    result = await my_async_function()
    assert result == expected_value


# Using async fixtures
@pytest.fixture
async def async_resource():
    resource = await create_resource()
    yield resource
    await resource.close()


async def test_with_async_fixture(async_resource):
    result = await async_resource.operation()
    assert result == expected_value
```

### Running Async Tests

```bash
# Run all tests (including async tests)
uv run pytest

# Run specific async tests
uv run pytest test_async_module.py
```

## Examples

### Testing an Async API Client

```python
import pytest


@pytest.fixture
async def api_client():
    client = AsyncAPIClient()
    await client.connect()
    yield client
    await client.disconnect()


async def test_api_get_data(api_client):
    data = await api_client.get_data("resource_id")
    assert "key" in data
    assert data["status"] == "active"
```

### Testing Concurrent Operations

```python
import asyncio


async def test_concurrent_operations():
    # Run multiple operations concurrently
    results = await asyncio.gather(operation1(), operation2(), operation3())

    # Check results
    assert results[0] == expected1
    assert results[1] == expected2
    assert results[2] == expected3
```

## Asyncio Modes

Pytest-asyncio supports different modes for handling the asyncio event loop:

1. **`auto`**: Automatically detects async tests and fixtures
2. **`strict`**: Requires explicit marking of async tests with `@pytest.mark.asyncio`
3. **`legacy`**: Uses a single event loop for all tests (deprecated)

## Best Practices

1. **Use appropriate fixtures**: Create async fixtures for resource management.
2. **Clean up resources**: Always clean up async resources in fixture teardown.
3. **Test error handling**: Test both success and error paths in async code.
4. **Avoid mixing sync and async**: Keep synchronous and asynchronous code separate.
5. **Test timeouts**: Use `asyncio.wait_for()` to test timeout behavior.
6. **Test cancellation**: Verify that your async code handles cancellation correctly.
7. **Use `asyncio.gather`**: Test concurrent operations with `asyncio.gather`.

## Common Issues and Solutions

| Issue                        | Solution                                                                   |
| ---------------------------- | -------------------------------------------------------------------------- |
| Event loop is closed         | Use `asyncio_mode = "auto"` in pytest configuration                        |
| Fixture teardown not running | Ensure you're using `yield` instead of `return` in async fixtures          |
| Test hangs indefinitely      | Add timeouts to your async operations with `asyncio.wait_for()`            |
| Mixing sync and async code   | Use `asyncio.run()` or `loop.run_until_complete()` to call async from sync |

## Resources

- [Pytest-asyncio Documentation](https://pytest-asyncio.readthedocs.io/)
- [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Asyncio Guide](https://realpython.com/async-io-python/)
