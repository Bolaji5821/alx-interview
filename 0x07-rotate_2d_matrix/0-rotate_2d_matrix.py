#!/usr/bin/env python3
"""Rotates a list lists clockwise"""


def rotate_2d_matrix(matrix):
    return [list(row[::-1]) for row in zip(*matrix)]
