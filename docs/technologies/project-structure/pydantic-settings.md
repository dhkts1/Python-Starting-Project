# Pydantic-Settings - Settings Management for Python

Pydantic-Settings is a library that provides a settings management system using Pydantic models, allowing for type-safe configuration with validation, environment variable support, and more.

## Overview

Pydantic-Settings helps manage application configuration by:

- Providing type validation for settings
- Supporting multiple configuration sources (env vars, .env files, etc.)
- Offering nested settings models
- Enabling environment-specific configurations
- Validating configuration values
- Supporting secrets management
- Integrating seamlessly with Pydantic

## Installation

Pydantic-Settings is included as a dependency:

```bash
# Install with other dependencies
uv sync
```

To install it directly:

```bash
uv pip install pydantic-settings
```

## How It's Used in This Project

In this project, Pydantic-Settings is used to:

1. Define and validate application configuration
2. Load settings from environment variables
3. Provide type-safe access to configuration values
4. Support different environments (development, testing, production)

## Configuration in This Project

Pydantic-Settings is typically used in a settings module:

```python
# src/utils/settings.py
from pathlib import Path
from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings.

    Provides a centralized configuration for the application with environment variable support.
    """

    APP_NAME: str = Field(
        default="Python Starting Project",
        description="The name of the application.",
    )
    APP_VERSION: str = Field(
        default="0.1.0",
        description="The version of the application.",
    )
    DEBUG: bool = Field(
        default=False,
        description="Enable or disable debug mode.",
    )
    LOG_LEVEL: str = Field(
        default="INFO",
        description="The logging level.",
    )
    LOG_FORMAT: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="The log message format.",
    )
    LOG_FILE: str = Field(
        default="logs/app.log",
        description="Path to the log file.",
    )

    # Paths
    BASE_DIR: Path = Field(
        default_factory=lambda: Path(__file__),
        description="Base directory of the application.",
    )
    LOG_DIR: Path = Field(
        default_factory=lambda: Path("logs"),
        description="Directory for log files.",
    )

    # Configuration source tracking
    env_file_found: bool = Field(
        default=False,
        description="Indicates whether a .env file was found during initialization.",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Create a global settings instance
settings = Settings()
```

## Basic Usage

### Defining Settings

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

    # Settings with types and default values
    debug: bool = False
    port: int = 8000
    api_key: str
    max_connections: int = 100
```

### Using Settings

```python
# Import the settings instance
from src.utils.settings import settings

# Access settings with type safety
if settings.DEBUG:
    print(f"Running in debug mode with log level {settings.LOG_LEVEL}")

# Use in application code
logger.info("Starting %s v%s", settings.APP_NAME, settings.APP_VERSION)
```

### Environment-Specific Settings

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "development"

    @property
    def is_development(self) -> bool:
        return self.environment == "development"

    @property
    def is_production(self) -> bool:
        return self.environment == "production"
```

### Environment Variable Override Behavior

In Pydantic-Settings, environment variables always take precedence over values in the `.env` file. This means that if a setting is defined both as an environment variable and in the `.env` file, the value from the environment variable will be used.

For example, if your `.env` file contains:

```
LOG_LEVEL=DEBUG
```

But you have an environment variable set:

```
LOG_LEVEL=INFO
```

The `LOG_LEVEL` setting will be `INFO`.

Pydantic settings consider the `extra` config in the case of dotenv files. If you set `extra=forbid` (the default) on `model_config` and your dotenv file contains an entry for a field that is not defined in the settings model, it will raise a `ValidationError`. For compatibility with Pydantic v1, you should use `extra=ignore`:

```python
model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore",
)
```

## Field Value Priority

In the case where a value is specified for the same `Settings` field in multiple ways, the selected value is determined as follows (in descending order of priority):

1. If `cli_parse_args` is enabled, arguments passed in at the CLI
2. Arguments passed to the `Settings` class initializer
3. Environment variables
4. Variables loaded from a dotenv (`.env`) file
5. Variables loaded from the secrets directory
6. Default field values for the `Settings` model

This priority order ensures that values can be overridden in a predictable way, with more explicit sources (like CLI arguments and initializer arguments) taking precedence over less explicit ones (like environment variables and dotenv files).

### Multiple Dotenv Files

If you need to load multiple dotenv files, you can pass multiple file paths as a tuple or list. The files will be loaded in order, with each file overriding the previous one:

```python
model_config = SettingsConfigDict(
    # `.env.prod` takes priority over `.env`
    env_file=(".env", ".env.prod")
)
```

This is useful for having a base configuration in one file and environment-specific overrides in another.

## Examples

### Environment Variables

```python
# Our settings support environment variables without a prefix
# For example, with these environment variables:
APP_NAME = "Environment App"
APP_VERSION = "2.0.0"
DEBUG = true
LOG_LEVEL = "DEBUG"

# The settings would be:
settings = Settings()
assert settings.APP_NAME == "Environment App"
assert settings.APP_VERSION == "2.0.0"
assert settings.DEBUG is True
assert settings.LOG_LEVEL == "DEBUG"
```

### Nested Settings

```python
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "user"
    password: str = "password"
    name: str = "database"


class AppSettings(BaseSettings):
    debug: bool = False
    database: DatabaseSettings = DatabaseSettings()
```

## Best Practices

1. **Use environment variables**: Store configuration in environment variables, especially for secrets.
2. **Provide defaults**: Set sensible default values for non-sensitive settings.
3. **Use validation**: Take advantage of Pydantic's validation to ensure settings are correct.
4. **Separate concerns**: Split settings into logical groups using nested models.
5. **Document settings**: Add docstrings to explain what each setting does.
6. **Use computed properties**: Add properties for derived values to keep settings DRY.
7. **Keep secrets secure**: Never hardcode sensitive information; use environment variables or secret management tools.

## Advanced Features

### Field Customization

```python
from pydantic import Field
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # Simple field with description
    APP_NAME: str = Field(
        default="Python Starting Project",
        description="The name of the application.",
    )

    # Boolean field
    DEBUG: bool = Field(
        default=False,
        description="Enable or disable debug mode.",
    )

    # Field with complex default using default_factory
    LOG_DIR: Path = Field(
        default_factory=lambda: Path("logs"),
        description="Directory for log files.",
    )
```

## CLI Support

Pydantic-Settings v2 provides integrated CLI support, making it easy to define CLI applications using Pydantic models. There are two primary use cases:

1. Using a CLI to override fields in Pydantic models
2. Using Pydantic models to define CLIs

To enable CLI parsing, set the `cli_parse_args` flag in the model configuration:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(cli_parse_args=True)

    debug: bool = False
    port: int = 8000
```

This allows you to override settings via command-line arguments:

```bash
python app.py --debug=true --port=9000
```

CLI arguments have the highest priority in the field value resolution order, taking precedence over all other sources.

## Customizing Settings Sources

If the default order of priority doesn't match your needs, you can change it by overriding the `settings_customise_sources` method of your `Settings` class:

```python
from typing import Tuple, Type
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


class Settings(BaseSettings):
    # Your settings fields here...

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        # Change the order of sources (first has highest priority)
        return env_settings, init_settings, dotenv_settings, file_secret_settings
```

This example changes the priority order so that environment variables take precedence over initializer arguments.

You can also add your own custom sources or remove existing ones by modifying the returned tuple.

## Resources

- [Pydantic-Settings Documentation](https://docs.pydantic.dev/latest/usage/pydantic_settings/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [12-Factor App Configuration](https://12factor.net/config)
- [Environment Variables Best Practices](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
