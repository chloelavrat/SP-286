"""
time_formatter.py - A module for formatting time in various ways.

Example Usage:
--------------

```python
from time_formatter import format_time, format_duration
print(format_time('2021-07-20T15:20:36', time_format='12h'))
# '07/20/2021 03:20 PM'
print(format_duration(seconds=12345))
# '3 hours, 25 minutes, 45 seconds'
```
"""

import datetime


def format_time(timestamp, time_format='24h'):
    """
    Format a given timestamp in a human-readable way.

    Parameters:
        timestamp (str or datetime.datetime): The timestamp in ISO 8601
            format or a Python datetime object.
        time_format (str): The desired time format. Options: '12h'
            for 12-hour clock, '24h' for 24-hour clock (default).

    Returns:
        str: The formatted timestamp in the specified time format.

    Example:

    ```python
    format_time('2021-07-20T15:20:36', time_format='12h')
    # '07/20/2021 03:20 PM'
    ```
    """
    if isinstance(timestamp, str):
        timestamp = datetime.datetime.fromisoformat(timestamp)

    if time_format == '12h':
        return timestamp.strftime('%m/%d/%Y %I:%M %p')
    elif time_format == '24h':
        return timestamp.strftime('%m/%d/%Y %H:%M')
    else:
        raise ValueError("Invalid time_format. Use '12h' or '24h'.")


def format_duration(seconds):
    """
    Format a duration in seconds into a human-readable format.

    Parameters:
        seconds (int): The duration in seconds.

    Returns:
        str: The formatted duration string in a human-readable format.

    Example:

    ```python
    format_duration(seconds=12345)
    # '3 hours, 25 minutes, 45 seconds'
    ```
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_duration = ""
    if hours > 0:
        formatted_duration += \
            f"{hours} {'hour' if hours == 1 else 'hours'}"
    if minutes > 0:
        formatted_duration += \
            f", {minutes} {'minute' if minutes == 1 else 'minutes'}"
    if seconds > 0:
        formatted_duration += \
            f", {seconds} {'second' if seconds == 1 else 'seconds'}"

    return formatted_duration.lstrip(", ")
