#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    """
    Define an attribute for an object if it doesn't already exist.

    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute already exists on the object.
    """
    if not hasattr(obj, attribute):     
        setattr(obj, attribute, value)
    else:
        raise TypeError("Can't add a new attribute")


class MyClass:
    pass

if __name__ == "__main__":
    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)
    
    try:
        a = "My String"
        add_attribute(a, "name", "Bob")  
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
