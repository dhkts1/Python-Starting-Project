"""Settings module for the application.

This module provides a flexible and type-safe way to manage application settings.
"""

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

    def __init__(self, **kwargs: Any) -> None:  # noqa: ANN401
        """Initialize settings and check for .env file.

        Args:
            **kwargs: Keyword arguments passed to the parent class constructor

        """
        # Check if .env file exists before initialization
        env_file_path = Path(".env")
        env_file_exists = env_file_path.exists()

        # Pass to parent constructor
        super().__init__(**kwargs)

        # Store whether .env file was found
        self.env_file_found = env_file_exists


# Create a global instance of the settings
settings = Settings()
