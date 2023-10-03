#!/usr/bin/python3
"""Represent a class."""


class Rectangle:
    """Define a class."""
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def dict(self):
        return {'width': self.width, 'height': self.height}


# Example usage:
if __name__ == "__main__":
    myrectangle = Rectangle(2, 4)
    print("Width:", myrectangle.width)
    print("Height:", myrectangle.height)
    print("Dictionary:", myrectangle.dict())
