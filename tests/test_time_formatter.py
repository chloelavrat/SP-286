"""Unittest for the module named time.formatter."""

import unittest
from APOLLO_LIBRARY.time.formatter import format_time, format_duration


class Test_TimeFormatter(unittest.TestCase):
    """
    Test cases for the time formatting functions in the
    my_pypi_package.time.formatter module.
    """

    def test_format_time_12h(self):
        """
        Test format_time function with 12-hour clock format.
        """
        self.assertEqual(
            format_time('2021-07-20T15:20:36', time_format='12h'),
            '07/20/2021 03:20 PM'
        )

    def test_format_time_24h(self):
        """
        Test format_time function with 24-hour clock format.
        """
        self.assertEqual(
            format_time('2021-07-20T15:20:36', time_format='24h'),
            '07/20/2021 15:20'
        )

    def test_format_duration(self):
        """
        Test format_duration function with a duration of 12345 seconds.
        """
        self.assertEqual(
            format_duration(12345),
            '3 hours, 25 minutes, 45 seconds'
        )


if __name__ == '__main__':
    unittest.main()
