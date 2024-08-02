"""
Text Replacement and File Renaming Utility

This Python script provides a command-line utility for performing text
replacement within files and renaming files and directories based on specified 
text. It is particularly useful for projects that require batch updating of 
file content and names, such as refactoring codebases or updating documentation.

Functionality:
1. Replace specific text within files that have `.py` and `.md` extensions.
2. Rename files and directories based on the specified old and new text.
3. Traverse directories recursively to apply changes throughout a project.

Main Functions:
- `update_text_in_file(filepath, target_text, replacement_text)`: Updates 
  all instances of a specified text within a file.
- `modify_and_rename(directory_path, old_text, new_text)`: Recursively 
  modifies file names and replaces text within files in a directory.
- `execute()`: Parses command-line arguments and triggers the text replacement 
  and renaming operations.

Usage:
- Basic usage: 
    ```bash
    python script.py --old old_text --new new_text
    ```
- Specify a starting directory:
    ```bash
    python script.py -d /path/to/directory --old old_text --new new_text
    ```
"""

import argparse
import glob
import os


def update_text_in_file(filepath, target_text, replacement_text):
    """
    Update all instances of a specified text within a file.

    Opens the file located at `filepath`, reads its content, and replaces
    every occurrence of `target_text` with `replacement_text`. The updated
    content is then saved back to the file.

    Args:
        filepath (str): Path to the target file.
        target_text (str): Text to be replaced.
        replacement_text (str): New text to replace the old text.

    Example:
        >>> update_text_in_file("sample.txt", "hello", "world")
        This will replace "hello" with "world" in "sample.txt".
    """
    with open(filepath, "r", encoding="utf-8-sig") as file:
        data = file.read()

    updated_data = data.replace(target_text, replacement_text)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(updated_data)


def modify_and_rename(directory_path, old_text, new_text):
    """
    Recursively modify file names and replace text within files in a directory.

    This function traverses the given `directory_path` and updates the names
    of files and directories. It also replaces occurrences of `old_text` with
    `new_text` in the content of files with .py and .md extensions.

    Args:
        directory_path (str): Root directory to start the search.
        old_text (str): Text to be replaced.
        new_text (str): Text to use as the replacement.

    Example:
        >>> modify_and_rename("workspace", "old_name", "new_name")
        This will update names and replace text from "old_name" to "new_name" in "workspace".
    """
    all_paths = glob.glob(os.path.join(directory_path, "**"), recursive=True)

    # Update text in .py and .md files
    for path in all_paths:
        if "__pycache__" not in path:
            if path.endswith(".py") or path.endswith(".md"):
                update_text_in_file(path, old_text, new_text)

    # Rename directories
    for path in all_paths:
        if "__pycache__" not in path and os.path.isdir(path):
            if os.path.basename(path) == old_text:
                new_directory_path = os.path.join(
                    os.path.dirname(path), new_text)
                os.rename(path, new_directory_path)

    # Rename files
    for path in all_paths:
        if "__pycache__" not in path and os.path.isfile(path):
            if old_text in os.path.basename(path):
                new_file_path = os.path.join(
                    os.path.dirname(path),
                    os.path.basename(path).replace(old_text, new_text),
                )
                os.rename(path, new_file_path)


def execute():
    """
    Command-line utility for text replacement and renaming operations.

    This function parses command-line arguments to determine the starting
    directory (`dir`), the text to be replaced (`old`), and the new text
    (`new`) for performing the operations.

    Example:
        To execute the script, use:
        ```python script.py --old old_text --new new_text```

        To specify a different starting directory, use:
        ```python script.py -d /path/to/directory --old old_text --new new_text```
    """
    parser = argparse.ArgumentParser(
        description="Perform text replacement and renaming operations."
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=".",
        help="Directory where operations will start",
    )
    parser.add_argument("--old", type=str, required=True,
                        help="Text to be replaced")
    parser.add_argument(
        "--new", type=str, required=True, help="Text to replace the old text with"
    )
    arguments = parser.parse_args()

    modify_and_rename(arguments.directory, arguments.old, arguments.new)


if __name__ == "__main__":
    execute()
