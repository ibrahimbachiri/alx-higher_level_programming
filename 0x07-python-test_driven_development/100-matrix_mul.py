#!/usr/bin/python3
"""Defines a function that multiplies all elements of a matrix.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (matrix): first matrix.
        m_b (matrix): second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If one element of those list of lists is not an integer
        or a float.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b is not a rectangle (all ‘rows’ should be,
        of the same size).
        ValueError: If m_a and m_b can’t be multiplied.

    Returns:
        matrrix: Product of the two matrices.
    """
    list_err = "{} must be a list"
    lists_err = "{} must be a list of lists"
    empty_err = "{} can't be empty"
    type_err = "{} should contain only integers or floats"
    size_err = "each row of {} must be of the same size"
    value_err = "{} and {} can't be multiplied"

    if not isinstance(m_a, list):
        raise TypeError(list_err.format('m_a'))

    if not isinstance(m_b, list):
        raise TypeError(list_err.format('m_b'))

    for element in m_a:
        if not isinstance(element, list):
            raise TypeError(lists_err.format('m_a'))

    for element in m_b:
        if not isinstance(element, list):
            raise TypeError(lists_err.format('m_b'))

    if len(m_a) == 0 or type(m_a[0]) is list and len(m_a[0]) == 0:
        raise ValueError(empty_err.format('m_a'))
    if len(m_b) == 0 or type(m_b[0]) is list and len(m_b[0]) == 0:
        raise ValueError(empty_err.format('m_b'))

    for element in m_a:
        for item in element:
            if not type(item) in (int, float):
                raise TypeError(type_err.format('m_a'))

    for element in m_b:
        for item in element:
            if not type(item) in (int, float):
                raise TypeError(type_err.format('m_b'))

    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])

    length = 0

    for element in m_a:
        if length != 0 and length != len(element):
            raise TypeError(size_err.format('m_a'))
        length = len(element)

    length = 0

    for element in m_b:
        if length != 0 and length != len(element):
            raise TypeError(size_err.format('m_b'))
        length = len(element)

    if len_m_a != len(m_b):
        raise ValueError(value_err.format('m_a', 'm_b'))

    new_matrix = [[0 for a in m_b[0]] for x in m_a]
    for i in range(len(m_a)):
        for n in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][n] += m_a[i][k] * m_b[k][n]

    return new_matrix
