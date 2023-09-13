#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    # Initialize variables to store the sum of products and the sum of weights
    sum_products = 0
    sum_weights = 0

    # Iterate through the tuples in the list and calculate the sum of products and weights
    for score, weight in my_list:
        sum_products += score * weight
        sum_weights += weight

    # Calculate and return the weighted average
    return sum_products / sum_weights
