<!-- markdownlint-disable -->

<a href="https://github.com/velvet-compute/velvet-lib/blob/main/APOLLO_LIBRARY/time/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `time`
My library. 

**Global Variables**
---------------
- **time**
- **time_ns**
- **timezone**
- **altzone**
- **daylight**
- **tzname**
- **CLOCK_REALTIME**
- **CLOCK_MONOTONIC**
- **CLOCK_MONOTONIC_RAW**
- **CLOCK_PROCESS_CPUTIME_ID**
- **CLOCK_THREAD_CPUTIME_ID**
- **CLOCK_BOOTTIME**
- **CLOCK_TAI**


---

<a href="https://github.com/velvet-compute/velvet-lib/blob/main/APOLLO_LIBRARY/time/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `struct_time`
The time value as returned by gmtime(), localtime(), and strptime(), and accepted by asctime(), mktime() and strftime().  May be considered as a sequence of 9 integers. 

Note that several fields' values are not the same as those defined by the C language standard for struct tm.  For example, the value of the field tm_year is the actual year, not year - 1900.  See individual fields' descriptions for details. 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
