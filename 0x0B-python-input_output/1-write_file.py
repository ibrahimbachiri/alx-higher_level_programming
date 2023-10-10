#!/usr/bin/python3
"""defining write_file with two arguments"""


def write_file(filename="",text=""):
    """learn filename."""
    with open(filename,"w",encoding='utf-8') as f:
        return f.write(text)
