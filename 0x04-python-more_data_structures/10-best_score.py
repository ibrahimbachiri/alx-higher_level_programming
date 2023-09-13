#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # Use the max() function with a custom key function to find the key with the largest value
        best_key = max(a_dictionary, key=lambda k: a_dictionary[k])
        return best_key
    else:
        return None
