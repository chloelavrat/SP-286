"""
# utils.py - A utility module for time formatting and duration representation.

Example Usage:
--------------

```python
from utils import pretty_time, pretty_duration
print(pretty_time('2021-07-20T15:20:36', format_style='12h'))
#'07/20/2021 03:20 PM'
print(pretty_duration(12345))
#'3 hours, 25 minutes, 45 seconds'
```
"""

import datetime


def pretty_time(timestamp, format_style="24h"):
    """
    Convert a timestamp into a user-friendly time string.

    Parameters:
        timestamp (str or datetime.datetime): The input timestamp, either as an ISO 8601 string
            or a Python datetime object.
        format_style (str): The format for the time representation. Choices: '12h'
            for a 12-hour clock, '24h' for a 24-hour clock (default).

    Returns:
        str: The timestamp formatted according to the specified style.

    Example:

    ```python
    pretty_time('2021-07-20T15:20:36', format_style='12h')
    # '07/20/2021 03:20 PM'
    ```
    """
    if isinstance(timestamp, str):
        timestamp = datetime.datetime.fromisoformat(timestamp)

    if format_style == "12h":
        return timestamp.strftime("%m/%d/%Y %I:%M %p")
    elif format_style == "24h":
        return timestamp.strftime("%m/%d/%Y %H:%M")
    else:
        raise ValueError("Invalid format_style. Use '12h' or '24h'.")


def pretty_duration(total_seconds):
    """
    Convert a duration in seconds into a readable format.

    Parameters:
        total_seconds (int): The duration in seconds.

    Returns:
        str: A formatted string representing the duration in hours, minutes, and seconds.

    Example:

    ```python
    pretty_duration(12345)
    # '3 hours, 25 minutes, 45 seconds'
    ```
    """
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    duration_parts = []
    if hours > 0:
        duration_parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes > 0:
        duration_parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds > 0:
        duration_parts.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    return ", ".join(duration_parts)
