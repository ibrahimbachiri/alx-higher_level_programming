#!/usr/bin/python3
"""Represent a class int."""


class MyInt(int):
    """class that inherits from int"""

    def __init__(self, value):
        """for initialiaze a value my init."""

        super().__init__()
        self.value = value

    """Define a self."""
    def __eq__(self, other):
        return self.value != other

    """Define other."""
    def __ne__(self, other):
        return self.value == other                                                
