#!/usr/bin/python3
"""Represent a matrix."""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    
    num_rows_a = len(m_a)
    num_cols_a = len(m_a[0]) if m_a else 0
    num_rows_b = len(m_b)
    num_cols_b = len(m_b[0]) if m_b else 0
    
    if not all(isinstance(val, (int, float)) for row in m_a for val in row) or not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    
    if not all(len(row) == num_cols_a for row in m_a) or not all(len(row) == num_cols_b for row in m_b):
        raise TypeError("Each row of m_a must be of the same size or each row of m_b must be of the same size")
    
    if num_cols_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = [[0 for _ in range(num_cols_b)] for _ in range(num_rows_a)]
    
    for i in range(num_rows_a):
        for j in range(num_cols_b):
            for k in range(num_cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
