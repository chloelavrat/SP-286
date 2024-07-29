# SP286 PyPI Template: A NASA Apollo Inspired Template

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python Versions](https://img.shields.io/badge/python-3.6%2C%203.10-blue.svg)

<div align="center">
  <img src="https://images.unsplash.com/photo-1672740276184-74e76b16c0f8?q=80&w=3328&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Banner" style="border-radius: 15px; width: 100%; max-width: 800px; height: auto;">
</div>

<h3 align="center">
  <b><a href="#">API Documentation</a></b>
  •
  <b><a href="#">Notebooks</a></b>
  •
  <b><a href="#">Guidelines</a></b>
</h3>

<p align="center"><b>SP286_LIB</b> is a template PyPI package designed to provide all the necessary components for creating your own package. Follow the instructions below to utilize it effectively in your projects. Note that this package is a placeholder, featuring only three modules that manage sample timestamps.</p>

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Versioning](#versioning)
- [Placeholder Functionality](#placeholder-functionality)
- [Acknowledgements](#acknowledgements)

## Installation

This template includes several essential shell scripts in the `scripts` directory to streamline the management and development of the library. Ensure Python is installed on your computer before proceeding.

### Steps to Use the Template:

1. **Change the Library Name:**
    ```bash
    python ./scripts/rename_package.py --old SP286_LIB --new YourNewLibraryName
    ```
    Example:
    ```bash
    python ./scripts/rename_package.py --old SP286_LIB --new Artemis_program
    ```

2. **Change the Library Version:**
    ```bash
    ./scripts/change_version.sh X.Y.Z
    ```
    For detailed versioning information, refer to the [Versioning](#versioning) section below.

3. **Create and Activate a Virtual Environment:**
    ```bash
    ./scripts/virtualenv_create.sh
    source ./scripts/virtualenv_activate.sh
    ```

4. **Develop Your Library:**
    
    Place your code in the `SP286_LIB/` directory. Ensure that `__init__.py` files are present in each directory and subdirectory of the library.

5. **Document Your Code:**
    
    Use the Google docstring format for all functions, classes, and files to ensure consistent and comprehensive documentation.

6. **Generate the Documentation:**
    ```bash
    ./scripts/generate_doc.sh
    ```
    Documentation will be available in the `/docs/API/` directory.

## Usage

To utilize the placeholder functionality, you can import the provided modules and use them as follows:

```python
from SP286_LIB.time.converter import unix_to_iso, iso_to_datetime

# Convert UNIX timestamp to ISO 8601 format
timestamp = 1626797436
iso_time = unix_to_iso(timestamp)
print(iso_time)  # Output: '2021-07-20T12:50:36'

# Convert ISO 8601 format to Python datetime object
iso_time = '2021-07-20T12:50:36'
datetime_obj = iso_to_datetime(iso_time)
print(datetime_obj)  # Output: datetime.datetime(2021, 7, 20, 12, 50, 36)
```

## Versioning

We follow Semantic Versioning (SemVer) for version numbering **vX.Y.Z**:

- **X**: Major version (backward-incompatible changes)
- **Y**: Minor version (backward-compatible new features)
- **Z**: Patch version (backward-compatible bug fixes)

When creating a new release:

1. Make necessary changes and improvements.
2. Update the version number in `setup.py`.
3. Commit your changes and push them to the repository.
4. Add a tag to the commit for the new version:
    ```bash
    git tag vX.Y.Z
    git push origin vX.Y.Z
    ```
This will trigger the CI process to build and publish the package on PyPI.

## Placeholder Functionality

The **SP286_LIB** template includes utility functions for handling time-related tasks, such as time conversion, calculations, and formatting. The `time_converter` module enables conversions between various time formats, including UNIX timestamps, ISO 8601, and Python datetime objects.

## Acknowledgements

Special thanks to the Apollo team for their insightful guide on efficient production methods. Their comprehensive approach and innovative solutions significantly enhance productivity and operational efficiency. If you are curious, the report is available [here](https://ntrs.nasa.gov/citations/19720005243).
