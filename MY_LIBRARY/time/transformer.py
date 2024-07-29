"""
transformer.py - A module for converting between various time representations.

Supported time formats:
- Epoch timestamp (seconds since January 1, 1970)
- ISO 8601 date-time format (e.g., 'YYYY-MM-DDTHH:MM:SS')
- Python datetime object

Example Usage:
--------------

```python
from transformer import epoch_to_iso, iso_to_datetime_obj, datetime_to_epoch
print(epoch_to_iso(1626797436))
# '2021-07-20T12:50:36'
print(iso_to_datetime_obj('2021-07-20T12:50:36'))
# datetime.datetime(2021, 7, 20, 12, 50, 36)
print(datetime_to_epoch(datetime.datetime(2021, 7, 20, 12, 50, 36)))
# 1626797436
```
"""

import datetime

def epoch_to_iso(epoch_seconds):
    """
    Transform an epoch timestamp into the ISO 8601 date-time format with timezone info.

    Parameters:
        epoch_seconds (int or float): The epoch timestamp
        (seconds since January 1, 1970).

    Returns:
        str: The date and time in ISO 8601 format with timezone information.

    Example:

    ```python
    epoch_to_iso(1626797436)
    # '2021-07-20T12:50:36+00:00'
    ```
    """
    dt_utc = datetime.datetime.fromtimestamp(epoch_seconds, tz=datetime.timezone.utc)
    return dt_utc.isoformat()


def iso_to_datetime_obj(iso_string):
    """
    Convert an ISO 8601 date-time string to a Python datetime object with timezone info.

    Parameters:
        iso_string (str): The date-time string in ISO 8601 format.

    Returns:
        datetime.datetime: The equivalent Python datetime object with timezone info.

    Example:

    ```python
    iso_to_datetime_obj('2021-07-20T12:50:36+00:00')
    # datetime.datetime(2021, 7, 20, 12, 50, 36, tzinfo=datetime.timezone.utc)
    ```
    """
    return datetime.datetime.fromisoformat(iso_string)


def datetime_to_epoch(dt_obj):
    """
    Convert a Python datetime object with timezone info to an epoch timestamp.

    Parameters:
        dt_obj (datetime.datetime): The Python datetime object with timezone info.

    Returns:
        int: The epoch timestamp (seconds since January 1, 1970).

    Example:

    ```python
    from datetime import datetime, timezone
    dt_obj = datetime(2021, 7, 20, 12, 50, 36, tzinfo=timezone.utc)
    datetime_to_epoch(dt_obj)
    # 1626797436
    ```
    """
    if dt_obj.tzinfo is None:
        raise ValueError("datetime object must be timezone-aware")
    return int(dt_obj.timestamp())
