"""
# operations.py - A module for handling time computations.

Example Usage:
--------------

```python
from operations import increase_time, decrease_time
print(increase_time('2021-07-20T12:50:36', hours=2, minutes=30))
# '2021-07-20T15:20:36'
print(decrease_time('2021-07-20T12:50:36', days=1))
# '2021-07-19T12:50:36'
```
"""

import datetime


def increase_time(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    """
    Add a specified duration to a given timestamp.

    Parameters:
        timestamp (str or datetime.datetime): The timestamp in ISO 8601 format or a datetime object.
        years (int): Number of years to add (default is 0).
        months (int): Number of months to add (default is 0).
        days (int): Number of days to add (default is 0).
        hours (int): Number of hours to add (default is 0).
        minutes (int): Number of minutes to add (default is 0).
        seconds (int): Number of seconds to add (default is 0).

    Returns:
        str: The updated timestamp after adding the specified duration in ISO 8601 format.

    Example:

    ```python
    increase_time('2021-07-20T12:50:36', hours=2, minutes=30)
    # '2021-07-20T15:20:36'
    ```
    """
    if isinstance(timestamp, str):
        timestamp = datetime.datetime.fromisoformat(timestamp)

    # Calculate the timedelta for years and months
    year_delta = datetime.timedelta(days=years * 365)

    # Approximate number of days in a month
    month_delta = datetime.timedelta(days=months * 30)

    # Aggregate all deltas to determine the final duration to add
    total_delta = datetime.timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    ) + year_delta + month_delta

    new_timestamp = timestamp + total_delta
    return new_timestamp.isoformat()


def decrease_time(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    """
    Subtract a specified duration from a given timestamp.

    Parameters:
        timestamp (str or datetime.datetime): The initial timestamp in
            ISO 8601 format or a datetime object.
        years (int): Number of years to subtract (default is 0).
        months (int): Number of months to subtract (default is 0).
        days (int): Number of days to subtract (default is 0).
        hours (int): Number of hours to subtract (default is 0).
        minutes (int): Number of minutes to subtract (default is 0).
        seconds (int): Number of seconds to subtract (default is 0).

    Returns:
        str: The updated timestamp after subtracting the specified duration in ISO 8601 format.

    Example:

    ```python
    decrease_time('2021-07-20T12:50:36', days=1)
    # '2021-07-19T12:50:36'
    ```
    """
    if isinstance(timestamp, str):
        timestamp = datetime.datetime.fromisoformat(timestamp)

    # Calculate the timedelta for years and months
    year_delta = datetime.timedelta(days=years * 365)
    month_delta = datetime.timedelta(days=months * 30)

    # Aggregate all deltas to determine the final duration to subtract
    total_delta = datetime.timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    ) + year_delta + month_delta

    new_timestamp = timestamp - total_delta
    return new_timestamp.isoformat()
