#!/usr/bin/env python
"""
Drive a game of Tic Tac Toe
"""

# board: map of cells to values

ROWS = 3
COLUMNS = 3


def print_board(board):
    """
    board: {(x: int, y: int): value
    """
    print(end="\n")
    for row in range(COLUMNS):
        for column in range(ROWS):
            print(board[(row, column)], end=" ")
        print(end="\n")
