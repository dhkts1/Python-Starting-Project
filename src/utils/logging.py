"""Logging module for the application.

This module provides a flexible and configurable logging setup.
"""

import logging
import sys
from pathlib import Path

from .settings import settings

# Module logger
logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Set up logging configuration."""
    # Create log directory if it doesn't exist
    log_file = Path(settings.LOG_FILE)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOG_LEVEL)

    # Clear existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create formatter
    formatter = logging.Formatter(settings.LOG_FORMAT)

    # Add console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Add file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    # Log configuration source
    logger = get_logger(__name__)
    logger.info("Logging initialized at level: %s", settings.LOG_LEVEL)


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific module.

    Args:
        name: The name of the module.

    Returns:
        A logger instance.

    """
    return logging.getLogger(name)
