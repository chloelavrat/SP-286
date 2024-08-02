<!-- markdownlint-disable -->

# API Overview

## Modules

- [`time`](./time.md#module-time): My library.
- [`time.calculator`](./time.calculator.md#module-timecalculator): calculator.py - A module for performing time-related calculations.
- [`time.converter`](./time.converter.md#module-timeconverter): converter.py - A module for converting time between different formats.
- [`time.formatter`](./time.formatter.md#module-timeformatter): time_formatter.py - A module for formatting time in various ways.

## Classes

- [`time.struct_time`](./time.md#class-struct_time): The time value as returned by gmtime(), localtime(), and strptime(), and

## Functions

- [`calculator.add_time`](./time.calculator.md#function-add_time): Add a specific duration to a given timestamp value.
- [`calculator.subtract_time`](./time.calculator.md#function-subtract_time): Subtract a specific duration from a given timestamp.
- [`converter.datetime_to_unix`](./time.converter.md#function-datetime_to_unix): Convert a Python datetime object to a UNIX timestamp.
- [`converter.iso_to_datetime`](./time.converter.md#function-iso_to_datetime): Convert an ISO 8601 date-time string to a Python datetime object.
- [`converter.unix_to_iso`](./time.converter.md#function-unix_to_iso): Convert a UNIX timestamp to the ISO 8601 date-time format.
- [`formatter.format_duration`](./time.formatter.md#function-format_duration): Format a duration in seconds into a human-readable format.
- [`formatter.format_time`](./time.formatter.md#function-format_time): Format a given timestamp in a human-readable way.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
