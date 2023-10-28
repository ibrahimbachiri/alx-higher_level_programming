#!/usr/bin/python3
"""defining to_json_string function."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8) and returns the number of characters added."""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
