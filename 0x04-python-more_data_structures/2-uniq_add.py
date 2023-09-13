#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate through the elements in the input list
    for element in my_list:
        # Check if the element is not in the set of unique integers
        if element not in unique_integers:
            # Add the element to the set of unique integers
            unique_integers.add(element)
            # Add the element to the total sum
            total_sum += element

    return total_sum
