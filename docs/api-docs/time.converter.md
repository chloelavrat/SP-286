<!-- markdownlint-disable -->

<a href="https://github.com/APOLLO_LIBRARY/time/converter.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `time.converter`
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


---

<a href="https://github.com/APOLLO_LIBRARY/time/converter.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unix_to_iso`

```python
unix_to_iso(unix_timestamp)
```

Convert a UNIX timestamp to the ISO 8601 date-time format. 



**Parameters:**
 
 - <b>`unix_timestamp`</b> (int or float):  The UNIX timestamp (seconds since January 1, 1970). 



**Returns:**
 
 - <b>`str`</b>:  The corresponding date and time in the ISO 8601 format. 



**Example:**
 

```python
unix_to_iso(1626797436)
# '2021-07-20T12:50:36'
``` 


---

<a href="https://github.com/APOLLO_LIBRARY/time/converter.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `iso_to_datetime`

```python
iso_to_datetime(iso_timestamp)
```

Convert an ISO 8601 date-time string to a Python datetime object. 



**Parameters:**
 
 - <b>`iso_timestamp`</b> (str):  The date-time string in the ISO 8601 format. 



**Returns:**
 
 - <b>`datetime.datetime`</b>:  The corresponding Python datetime object. 



**Example:**
 

```python
iso_to_datetime('2021-07-20T12:50:36')
# datetime.datetime(2021, 7, 20, 12, 50, 36)
``` 


---

<a href="https://github.com/APOLLO_LIBRARY/time/converter.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `datetime_to_unix`

```python
datetime_to_unix(dt)
```

Convert a Python datetime object to a UNIX timestamp. 



**Parameters:**
 
 - <b>`dt`</b> (datetime.datetime):  The Python datetime object. 



**Returns:**
 
 - <b>`int`</b>:  The UNIX timestamp (seconds since January 1, 1970). 



**Example:**
 

```python
from datetime import datetime
dt = datetime(2021, 7, 20, 12, 50, 36)
datetime_to_unix(dt)
# 1626797436
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
