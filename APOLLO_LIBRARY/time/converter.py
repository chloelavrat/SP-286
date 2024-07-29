"""
converter.py - A module for converting time between different formats.

Supported time formats:
- UNIX timestamp (seconds since January 1, 1970)
- ISO 8601 date-time format (e.g., 'YYYY-MM-DDTHH:MM:SS')
- Python datetime object

Example Usage:
--------------

```python
from time.converter import unix_to_iso, iso_to_datetime
print(unix_to_iso(1626797436))
# '2021-07-20T12:50:36'
print(iso_to_datetime('2021-07-20T12:50:36'))
# datetime.datetime(2021, 7, 20, 12, 50, 36)
```

"""

import datetime


def unix_to_iso(unix_timestamp):
    """
    Convert a UNIX timestamp to the ISO 8601 date-time format.

    Parameters:
        unix_timestamp (int or float): The UNIX timestamp
        (seconds since January 1, 1970).

    Returns:
        str: The corresponding date and time in the ISO 8601 format.

    Example:

    ```python
    unix_to_iso(1626797436)
    # '2021-07-20T12:50:36'
    ```
    """
    return datetime.datetime.utcfromtimestamp(unix_timestamp).isoformat()


def iso_to_datetime(iso_timestamp):
    """
    Convert an ISO 8601 date-time string to a Python datetime object.

    Parameters:
        iso_timestamp (str): The date-time string in the ISO 8601 format.

    Returns:
        datetime.datetime: The corresponding Python datetime object.

    Example:

    ```python
    iso_to_datetime('2021-07-20T12:50:36')
    # datetime.datetime(2021, 7, 20, 12, 50, 36)
    ```
    """
    return datetime.datetime.fromisoformat(iso_timestamp)


def datetime_to_unix(dt):
    """
    Convert a Python datetime object to a UNIX timestamp.

    Parameters:
        dt (datetime.datetime): The Python datetime object.

    Returns:
        int: The UNIX timestamp (seconds since January 1, 1970).

    Example:

    ```python
    from datetime import datetime
    dt = datetime(2021, 7, 20, 12, 50, 36)
    datetime_to_unix(dt)
    # 1626797436
    ```
    """
    return int((dt - datetime.datetime(1970, 1, 1)).total_seconds())


# Additional functions for other time format conversions can be added here.
