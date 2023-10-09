#!/usr/bin/python3
"""Define an attribute."""


def add_attribute(obj, attribute, value):
    """Define an attribute."""

    if not hasattr(obj, attribute):

        setattr(obj, attribute, value)

    else:
        raise TypeError("can't add new attribute")

if __name__ == "__main__":
    """Represent a class."""


    class MyClass():
        pass

        mc = MyClass()
        add_attribute(mc, "name", "John")
        print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)

    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
