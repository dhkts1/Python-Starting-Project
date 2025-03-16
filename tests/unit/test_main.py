"""Tests for the main module."""

import unittest
from unittest.mock import MagicMock, patch

from src.main import main


class TestMain(unittest.TestCase):
    """Tests for the main function."""

    def test_main_exists(self) -> None:
        """Test that the main function exists."""
        assert callable(main)

    @patch("src.main.logger")
    @patch("src.main.settings")
    def test_main_logs_correctly(self, mock_settings: MagicMock, mock_logger: MagicMock) -> None:
        """Test that the main function logs the correct messages."""
        # Setup mock settings
        mock_settings.APP_NAME = "TestApp"
        mock_settings.APP_VERSION = "1.0.0"

        # Call the main function
        main()

        # Check that the logger was called with the correct messages
        mock_logger.info.assert_any_call("Starting %s v%s", "TestApp", "1.0.0")
        mock_logger.info.assert_any_call("Application finished")

    @patch("src.main.logger")
    @patch("src.main.settings")
    def test_main_uses_settings(self, mock_settings: MagicMock, mock_logger: MagicMock) -> None:
        """Test that the main function uses the settings correctly."""
        # Setup mock settings
        mock_settings.APP_NAME = "CustomApp"
        mock_settings.APP_VERSION = "2.3.4"

        # Call the main function
        main()

        # Check that the settings were used correctly
        mock_logger.info.assert_any_call("Starting %s v%s", "CustomApp", "2.3.4")
