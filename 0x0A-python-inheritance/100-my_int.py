#!/usr/bin/python3
"""Represent a class int."""


class MyInt(int):
    """class that inherits from int"""

    def __init__(self, value):
        """for initialiaze a value my init."""

        super().__init__()
        self.value = value

def __eq__(self, other):
    """Define a self."""
        return self.value != other

def __ne__(self, other):
    """Define other."""
        return self.value == other                                                
