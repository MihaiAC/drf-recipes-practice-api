"""
Test custom Django management commands.
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test wait_for_db if database is ready."""
        patched_check.return_value = True
        call_command("wait_for_db")

        # Check the mocked method has been called.
        patched_check.assert_called_once_with(databases=["default"])

    # Mock sleep, so the tests won't take forever.
    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test wait_for_db when getting OperationalError."""
        # Throw a Psycopg2Error the first two times then OperationalError the next
        # three times.
        patched_check.side_effect = (
            [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        )
        call_command("wait_for_db")
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
