"""
calculator.py - A module for performing time-related calculations.

Example Usage:
--------------

```python
from time_calculator import add_time, subtract_time
print(add_time('2021-07-20T12:50:36', hours=2, minutes=30))
# '2021-07-20T15:20:36'
print(subtract_time('2021-07-20T12:50:36', days=1))
# '2021-07-19T12:50:36'
```

"""

import datetime


def add_time(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    """
    Add a specific duration to a given timestamp value.

    Parameters:
        timestamp (str or datetime.datetime):
            The timestamp in ISO 8601 format or a Python datetime object.
        years (int): Number of years to add (default is 0).
        months (int): Number of months to add (default is 0).
        days (int): Number of days to add (default is 0).
        hours (int): Number of hours to add (default is 0).
        minutes (int): Number of minutes to add (default is 0).
        seconds (int): Number of seconds to add (default is 0).

    Returns:
        str: The resulting timestamp after adding the specified
             duration in ISO 8601 format.

    Example:

    ```python
    add_time('2021-07-20T12:50:36', hours=2, minutes=30)
    # '2021-07-20T15:20:36'
    ```
    """
    if isinstance(timestamp, str):
        timestamp = datetime.datetime.fromisoformat(timestamp)

    # Calculate the timedelta for months and years
    years_delta = datetime.timedelta(days=years * 365)
    # Approximate number of days in a month
    months_delta = datetime.timedelta(days=months * 30)

    # Combine all deltas to get the final duration to add
    delta = (
        datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        + years_delta
        + months_delta
    )

    new_timestamp = timestamp + delta
    return new_timestamp.isoformat()


def subtract_time(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    """
    Subtract a specific duration from a given timestamp.

    Parameters:
        timestamp (str or datetime.datetime): The initial timestamp in
            ISO 8601 format or a Python datetime object.
        years (int): Number of years to subtract (default is 0).
        months (int): Number of months to subtract (default is 0).
        days (int): Number of days to subtract (default is 0).
        hours (int): Number of hours to subtract (default is 0).
        minutes (int): Number of minutes to subtract (default is 0).
        seconds (int): Number of seconds to subtract (default is 0).

    Returns:
        str: The resulting timestamp after subtracting the specified duration
             in ISO 8601 format.

    Example:

    ```python
    subtract_time('2021-07-20T12:50:36', days=1)
    # '2021-07-19T12:50:36'
    ```
    """
    if isinstance(timestamp, str):
        timestamp = datetime.datetime.fromisoformat(timestamp)

    # Calculate the timedelta for months and years
    years_delta = datetime.timedelta(days=years * 365)
    # Approximate number of days in a month
    months_delta = datetime.timedelta(days=months * 30)

    # Combine all deltas to get the final duration to subtract
    delta = (
        datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        + years_delta
        + months_delta
    )

    new_timestamp = timestamp - delta
    return new_timestamp.isoformat()


# Additional functions for other time-related calculations can be added here.
