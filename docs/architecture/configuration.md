# Configuration System

The configuration system is built around the `src/utils/settings.py` module, which provides a flexible and type-safe way to manage application settings.

## Features

- **Environment Variable Support**: Load configuration from environment variables
- **Dotenv Support**: Load configuration from `.env` file (environment variables take precedence if present)
- **Type Validation**: Ensure settings have the correct types
- **Default Values**: Provide sensible defaults for all settings
- **Directory Creation**: Automatically create required directories
- **Pydantic Integration**: Uses pydantic-settings for robust configuration management

## Project Configuration

The project uses `pyproject.toml` for configuration, which includes:

- **Project Metadata**: Name, version, description, and Python version requirements
- **Dependencies**: Core dependencies required for the application
- **Development Dependencies**: Tools for development, testing, and documentation
- **Tool Configuration**: Settings for various development tools

### Core Dependencies

The project depends on the following core packages:

```toml
[project]
dependencies = [
  "logging>=0.4.9.6",
  "pydantic-settings>=2.8.1",
  "lazy-loader>=0.4",
]

[dependency-groups]
dev = [
  "mdformat>=0.7.22",
  "codespell>=2.4.1",
  "flynt>=1.0.2",
  "mkdocs>=1.6.1",
  # ... and many more development dependencies
]
```

- **logging**: Provides logging functionality
- **pydantic-settings**: Used for configuration management with environment variables
- **lazy-loader**: Enables lazy loading of modules

### Development Tools

The project uses several development tools configured in `pyproject.toml`:

- **UV**: Fast Python package installer and resolver
- **Ruff**: Fast Python linter and formatter
- **Pyright**: Static type checker
- **Pre-commit**: Git hook scripts
- **Pytest**: Testing framework
- **MkDocs**: Documentation generator

### Tool Configuration

The `pyproject.toml` file includes configuration for:

- **Ruff**: Comprehensive linting and formatting rules
- **Pyright**: Static type checking in strict mode
- **UV**: Fast Python package installer and dependency management
- **Bandit**: Security linting configuration
- **Darglint**: Docstring style checking
- **Commitizen**: Conventional commit enforcement
- **Interrogate**: Docstring coverage checking
- **Vulture**: Dead code detection

## Usage

Settings can be accessed throughout the application by importing the `settings` instance:

```python
from utils.settings import settings

print(f"Application name: {settings.APP_NAME}")
print(f"Debug mode: {settings.DEBUG}")
```

## Available Settings

| Setting | Type | Default | Description |
| ------- | ---- | ------- | ----------- |
| `APP_NAME` | `str` | "Python Starting Project" | The name of the application |
| `APP_VERSION` | `str` | "0.1.0" | The version of the application |
| `DEBUG` | `bool` | `False` | Enable or disable debug mode |
| `LOG_LEVEL` | `str` | "INFO" | The logging level |
| `LOG_FORMAT` | `str` | "%(asctime)s - %(name)s - %(levelname)s - %(message)s" | The log message format |
| `LOG_FILE` | `str` | "logs/app.log" | Path to the log file |
| `BASE_DIR` | `Path` | `Path(__file__)` | Base directory of the application |
| `LOG_DIR` | `Path` | `Path("logs")` | Directory for log files |
| `env_file_found` | `bool` | `False` | Indicates whether a .env file was found during initialization |

## Adding New Settings

To add new settings to your application:

1. Add the setting with its type annotation and default value to the `Settings` class in `src/utils/settings.py`:

```python
class Settings(BaseSettings):
    # Existing settings...

    # New setting
    NEW_SETTING: str = Field(
        default="default value",
        description="Description of the new setting",
    )
```

2. Add the setting to `.env.example` with a comment explaining its purpose:

```
# New setting description
NEW_SETTING=default value
```

3. Use the setting in your code:

```python
from utils.settings import settings

print(f"New setting: {settings.NEW_SETTING}")
```

## Development Commands

The project includes several predefined commands that can be run using UV:

```bash
# Install dependencies
uv sync

# Run linting tools
uv run ruff check
uv run ruff format
uv run pyright
uv run pre-commit run --all-files

# Run tests with coverage
uv run pytest -x -n 4 --cov=src --cov-report=xml --fail-under=80 src

# Build documentation
uv run mkdocs build
uv run mkdocs serve

# Security checks
uv run bandit -c pyproject.toml -r src
uv run safety check
uv run vulture src --min-confidence 80
```
