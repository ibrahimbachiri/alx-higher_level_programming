#!/usr/bin/python3
"""Definition of an object."""


def lookup(obj):
    return dir(obj)

"""Definition of a class."""
class MyClass1(object):
    pass

"""Definition of a class."""
class MyClass2(object):
    my_attr1 = 3

def my_meth(self):
    pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))                            
