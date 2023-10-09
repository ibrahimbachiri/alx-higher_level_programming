#!/usr/bin/python3
"""Represent a class."""


class MyInt(int):

    """Define a value."""
    def __init__(self, value):

        super().__init__()
        self.value = value

    """Define a self."""
    def __eq__(self, other):
        return self.value != other

    """Define other."""
    def __ne__(self, other):
        return self.value == other                                                
