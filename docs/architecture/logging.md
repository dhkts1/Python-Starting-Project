# Logging System

The logging system is configured in `src/utils/logging.py`, which provides a flexible and configurable logging setup for your application.

## Features

- **Console and File Logging**: Log to both console and file
- **Configurable Log Levels**: Set log levels via settings
- **Automatic Directory Creation**: Create log directories if they don't exist
- **Structured Logging**: Consistent log format across the application
- **Module-specific Loggers**: Get loggers for specific modules

## Usage

To use logging in your application:

```python
from utils.logging import setup_logging, get_logger

# Initialize logging
setup_logging()

# Get a logger for your module
logger = get_logger(__name__)

# Log messages at different levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

## Configuration

The logging system can be configured through the following settings:

| Setting      | Type  | Default                                                | Description            |
| ------------ | ----- | ------------------------------------------------------ | ---------------------- |
| `LOG_LEVEL`  | `str` | "INFO"                                                 | The logging level      |
| `LOG_FORMAT` | `str` | "%(asctime)s - %(name)s - %(levelname)s - %(message)s" | The log message format |
| `LOG_FILE`   | `str` | "logs/app.log"                                         | Path to the log file   |

## Customizing Logging

To customize logging for your application:

# Modify the log format, level, or handlers in `src/utils/logging.py`:

```python
def setup_logging() -> None:
    """Set up logging configuration."""
    # Create custom formatter
    formatter = logging.Formatter(settings.LOG_FORMAT)

    # Add custom handlers
    # ...
```

# Add custom log filters or formatters as needed:

```python
class CustomFilter(logging.Filter):
    """Custom log filter."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter log records."""
        # Custom filtering logic
        return True
```

# Configure component-specific loggers using the `get_logger` function:

```python
# Get a logger for a specific component
logger = get_logger("component_name")

# Set component-specific log level
logger.setLevel(logging.DEBUG)
```
