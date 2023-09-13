#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the symmetric difference operation (^) to find elements present in only one set
    diff_set = set_1 ^ set_2
    return diff_set
