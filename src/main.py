"""Main module for the application."""

import logging

from src.utils.logging import setup_logging
from src.utils.settings import settings

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for the application."""
    logger.info("Starting %s v%s", settings.APP_NAME, settings.APP_VERSION)

    # Application logic goes here
    logger.info("Application finished")


if __name__ == "__main__":
    main()
