#!/usr/bin/python3
"""Class for Student creation"""

class Student:
    """Student object"""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the object to a JSON representation (dictionary)"""
        return self.__dict__

