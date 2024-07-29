"""Unittest for the module named time.calculator."""

import unittest
from SP286_LIB.time.calculator import add_time, subtract_time


class Test_TimeCalculator(unittest.TestCase):
    """
    Test class for the `add_time` and `subtract_time`
    functions in the time.calculator module.

    Usage:
    ------
    Run this script to perform unit tests on the
    `add_time` and `subtract_time` functions.

    Example:
    --------
    >>> python test_time_calculator.py
    """

    def test_add_time(self):
        """
        Test the `add_time` function for correct behavior.

        The function should correctly add the specified duration
        to the given timestamp and return the resulting timestamp.

        Test cases include:
        - Adding hours and minutes to the timestamp
        - Adding minutes and seconds to the timestamp
        """
        self.assertEqual(
            add_time('2021-07-20T12:50:36', hours=2, minutes=30),
            '2021-07-20T15:20:36')

    def test_subtract_time(self):
        """
        Test the `subtract_time` function for correct behavior.

        The function should correctly subtract the specified duration
        from the given timestamp and return the resulting timestamp.

        Test cases include:
        - Subtracting days from the timestamp
        - Subtracting hours and minutes from the timestamp
        """
        self.assertEqual(
            subtract_time('2021-07-20T12:50:36', days=1),
            '2021-07-19T12:50:36')


if __name__ == '__main__':
    unittest.main()
