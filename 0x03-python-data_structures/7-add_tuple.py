#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements of each tuple
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Sum the elements and return a new tuple
    result_tuple = (a1 + b1, a2 + b2)
    
    return result_tuple
