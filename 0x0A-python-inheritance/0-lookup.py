#!/usr/bin/python3


def lookup(obj):
    """
    Retrieve and return the list of attributes and methodes of an object.
    Args:
        obj: The object to look up.

    Returns:
        list: A list of strings containing attribute and method names.
    """
    return dir(obj)

class MyClass1(object):
    """
    Definition of MyClass1.

    This is a simple class with no attributes or methods.
    """
    pass

class MyClass2(object):
    """
    Definition of Myclass2.

    This class has an attribute 'my_attr1' and a method 'my_meth'.
    """

    my_attr1 = 3

def my_meth(self):
    """A placeholder method."""
    pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))                            
