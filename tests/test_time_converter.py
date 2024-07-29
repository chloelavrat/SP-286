"""Unittest for the module named time.converter."""

import unittest
from APOLLO_LIBRARY.time.converter import \
    unix_to_iso, iso_to_datetime, datetime_to_unix


class Test_TimeConverter(unittest.TestCase):
    def test_unix_to_iso(self):
        """
        Test the 'unix_to_iso' function.

        It checks if the function converts a UNIX timestamp
        to the correct ISO 8601 format.

        Example:
        >>> test_unix_to_iso(1626797436)
        '2021-07-20T16:10:36'
        """
        self.assertEqual(
            unix_to_iso(1626797436),
            '2021-07-20T16:10:36')

    def test_iso_to_datetime(self):
        """
        Test the 'iso_to_datetime' function.

        It checks if the function converts an ISO 8601 date-time
        string to a Python datetime object correctly.

        Example:
        >>> test_iso_to_datetime('2021-07-20T12:50:36')
        '2021-07-20T12:50:36'
        """
        self.assertEqual(
            iso_to_datetime('2021-07-20T12:50:36').isoformat(),
            '2021-07-20T12:50:36')

    def test_datetime_to_unix(self):
        """
        Test the 'datetime_to_unix' function.

        It checks if the function converts a Python datetime object
        to the correct UNIX timestamp.

        Example:
        >>> from datetime import datetime
        >>> dt = datetime(2021, 7, 20, 12, 50, 36)
        >>> test_datetime_to_unix(dt)
        1626785436
        """
        from datetime import datetime
        dt = datetime(2021, 7, 20, 12, 50, 36)
        self.assertEqual(
            datetime_to_unix(dt),
            1626785436)


if __name__ == '__main__':
    unittest.main()
