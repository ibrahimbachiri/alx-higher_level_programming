#!/usr/bin/python3
"""Defines an attribute."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): the object to add an attribute to.
        att (strf): the name of the attribute to add to obj.
        value (any): the value of att.
    Raises:
        typeError: if the attribute cannot be added.
    """
    if not hasattr(obj,"__dict__"):
        raise typeError("can't add new attribute")
    setattr(obj,att,value)
