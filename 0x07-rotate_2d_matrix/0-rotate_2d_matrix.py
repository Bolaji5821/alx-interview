#!/usr/bin/python3
"""Rotates a list lists clockwise"""


def rotate_2d_matrix(matrix):
    """function to rotate the matrix"""
    return [list(row[::-1]) for row in zip(*matrix)]
