<!-- markdownlint-disable -->

<a href="https://github.com/velvet-compute/velvet-lib/blob/main/APOLLO_LIBRARY/time/formatter.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `time.formatter`
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


---

<a href="https://github.com/velvet-compute/velvet-lib/blob/main/APOLLO_LIBRARY/time/formatter.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `format_time`

```python
format_time(timestamp, time_format='24h')
```

Format a given timestamp in a human-readable way. 



**Parameters:**
 
 - <b>`timestamp`</b> (str or datetime.datetime):  The timestamp in ISO 8601  format or a Python datetime object. 
 - <b>`time_format`</b> (str):  The desired time format. Options: '12h'  for 12-hour clock, '24h' for 24-hour clock (default). 



**Returns:**
 
 - <b>`str`</b>:  The formatted timestamp in the specified time format. 



**Example:**
 

```python
format_time('2021-07-20T15:20:36', time_format='12h')
# '07/20/2021 03:20 PM'
``` 


---

<a href="https://github.com/velvet-compute/velvet-lib/blob/main/APOLLO_LIBRARY/time/formatter.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `format_duration`

```python
format_duration(seconds)
```

Format a duration in seconds into a human-readable format. 



**Parameters:**
 
 - <b>`seconds`</b> (int):  The duration in seconds. 



**Returns:**
 
 - <b>`str`</b>:  The formatted duration string in a human-readable format. 



**Example:**
 

```python
format_duration(seconds=12345)
# '3 hours, 25 minutes, 45 seconds'
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
