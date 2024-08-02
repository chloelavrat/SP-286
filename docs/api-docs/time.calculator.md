<!-- markdownlint-disable -->

<a href="https://github.com/APOLLO_LIBRARY/time/calculator.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `time.calculator`
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


---

<a href="https://github.com/APOLLO_LIBRARY/time/calculator.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_time`

```python
add_time(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0)
```

Add a specific duration to a given timestamp value. 



**Parameters:**
  timestamp (str or datetime.datetime):  The timestamp in ISO 8601 format or a Python datetime object. 
 - <b>`years`</b> (int):  Number of years to add (default is 0). 
 - <b>`months`</b> (int):  Number of months to add (default is 0). 
 - <b>`days`</b> (int):  Number of days to add (default is 0). 
 - <b>`hours`</b> (int):  Number of hours to add (default is 0). 
 - <b>`minutes`</b> (int):  Number of minutes to add (default is 0). 
 - <b>`seconds`</b> (int):  Number of seconds to add (default is 0). 



**Returns:**
 
 - <b>`str`</b>:  The resulting timestamp after adding the specified  duration in ISO 8601 format. 



**Example:**
 

```python
add_time('2021-07-20T12:50:36', hours=2, minutes=30)
# '2021-07-20T15:20:36'
``` 


---

<a href="https://github.com/APOLLO_LIBRARY/time/calculator.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `subtract_time`

```python
subtract_time(
    timestamp,
    years=0,
    months=0,
    days=0,
    hours=0,
    minutes=0,
    seconds=0
)
```

Subtract a specific duration from a given timestamp. 



**Parameters:**
 
 - <b>`timestamp`</b> (str or datetime.datetime):  The initial timestamp in  ISO 8601 format or a Python datetime object. 
 - <b>`years`</b> (int):  Number of years to subtract (default is 0). 
 - <b>`months`</b> (int):  Number of months to subtract (default is 0). 
 - <b>`days`</b> (int):  Number of days to subtract (default is 0). 
 - <b>`hours`</b> (int):  Number of hours to subtract (default is 0). 
 - <b>`minutes`</b> (int):  Number of minutes to subtract (default is 0). 
 - <b>`seconds`</b> (int):  Number of seconds to subtract (default is 0). 



**Returns:**
 
 - <b>`str`</b>:  The resulting timestamp after subtracting the specified duration  in ISO 8601 format. 



**Example:**
 

```python
subtract_time('2021-07-20T12:50:36', days=1)
# '2021-07-19T12:50:36'
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
