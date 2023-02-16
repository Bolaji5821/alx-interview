#!/usr/bin/python3
"""Rotates a list lists clockwise"""


def rotate_2d_matrix(matrix):
    """function to rotate matrix clockwise"""
    if (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or not all(isinstance(row, list) for row in matrix)
    ):
        return
    rows, cols = len(matrix), len(matrix[0])
    if not all(len(row) == cols for row in matrix):
        return
    new_matrix = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_matrix[j][rows - i - 1] = matrix[i][j]
    matrix[:] = new_matrix
