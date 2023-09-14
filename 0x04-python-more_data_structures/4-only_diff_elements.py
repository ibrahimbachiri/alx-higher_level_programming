#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the intersection operation (&) to find common elements
    diff_set = set_1 ^ set_2
    return diff_set
