#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate through the rows in the input matrix
    for row in matrix:
        # Create a new row for the new matrix
        new_row = []
        # Iterate through the elements in the row and square each element
        for element in row:
            new_row.append(element ** 2)
        # Add the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix
