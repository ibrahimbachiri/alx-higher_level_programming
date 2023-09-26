#!/usr/bin/python3
"""import Math."""


import math
"""Represent a class."""


class MagicClass:
    """Define a self."""
    def __init__(self, radius=0):
        self.radius = 0
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.radius = float(radius)
            self.__radius = float(radius)
    """Define area."""
    def area(self):
        return self.__radius ** 2 * math.pi
    """Define self."""
    def circumference(self):
        return 2 * math.pi * self.__radius

