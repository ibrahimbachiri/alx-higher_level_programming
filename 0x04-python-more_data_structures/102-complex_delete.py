#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a list of keys to delete
    keys_to_delete = []

    # Iterate through the dictionary and identify keys with the specified value
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Delete the identified keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
