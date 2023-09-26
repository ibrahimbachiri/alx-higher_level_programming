#!/usr/bin/python3
"""Represent a class."""


class Square:
    """Define a size."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality operator (==)."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality operator (!=)."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less-than operator (<)."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less-than-or-equal operator (<=)."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater-than operator (>)."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater-than-or-equal operator (>=)."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
