#!/usr/bin/python3
'''module for lookup method'''


def lookup(obj):
    '''looks up object attributes and methods.
    Args:
        obj (object): the object to list.

    Returns:
            list: the list of attributes.
    '''
    return dir(obj)
