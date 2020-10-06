#!/usr/bin/env python
"""
Drive a game of Tic Tac Toe
"""

# board: map of cells to values

ROWS = 3
COLUMNS = 3

PLAYER_X = "X"
PLAYER_Y = "Y"
BLANK = " "

class State:

    def __init__(self, rows=ROWS, columns=COLUMNS):
        self.rows = rows
        self.columns = columns

        self.board = self._clear_board()
        self.turn = PLAYER_X
        self.status = "Playing"
        self.score = {PLAYER_X: 0, PLAYER_Y: 0}

    def reset(self):
        self.board = self._clear_board()
        self.turn = PLAYER_X
        self.status = "Playing"


    def _clear_board(self):
        return {(row, column): BLANK
                for row in range(self.rows)
                    for column in range(self.columns)}

    def open_square(self, xy):
        """
        Verify that the spot is not already taken
        """
        return self.board[xy] == BLANK

    def mark_square(self, player, xy):
        """
        Mark square.
        Check for win or draw status
        """
        self.board[xy] = player

    def has_player_won(self, player):
        """
        Brute force... someday I'll know better ways to do this.
        """
        player_set = set((player,))
        board = self.board
        # check 
        for row in range(self.rows):
            if set(board[(row, v)] for v in range(self.columns)) == player_set:
                return True

        for column in range(self.columns):
            if set(board[(v, column)] for v in range(self.rows)) == player_set:
                return True

        # back slash, assumes square
        if set(board[(v, v)] for v in range(self.rows)) == player_set:
            return True

        # forward slash, assumes square
        forward_slash = zip(range(self.rows), range(self.columns)[::-1])
        if set(board[xy] for xy in forward_slash) == player_set:
            return True

        return False

    def is_game_a_draw(self):
        """
        Check for conflict along any line
        """
        both_players = set((PLAYER_X, PLAYER_Y))
        board = self.board

        # check 
        all_rows = all( set(board[(row, v)] for v in range(self.columns)) == both
                                for row in range(self.rows) )
        all_columns = all( set(board[(v, column)] for v in range(self.rows)) == both
                                for column in range(self.columns) )

        # back slash, assumes square
        back_slash = (set(board[(v, v)] for v in range(self.rows)) == player_set)

        forward_slash_xys = zip(range(self.rows), range(self.columns)[::-1])
        forward_slash = (set(board[xy] for xy in forward_slash_xys) == player_set)

        return all((all_rows, all_columns, back_slash, forward_slash))



def print_board(board):
    """
    board: {(x: int, y: int): value
    """
    print(end="\n")
    for row in range(COLUMNS):
        for column in range(ROWS):
            print(board[(row, column)], end=" ")
        print(end="\n")


def parse_place(string):
    # clean
    y, x = string.split(",")
    try:
        row = int(y.strip())
        column = int(x.strip())
    except ValueError as e:
        print("Coordinates must be a comma separated pair of numbers, column first"
                "For example: 2, 1\n")
        return None
    return (row, column)


def game_loop():
    """
    Start game
    """
    state = State()
    print("Coordinates are zero based")
    print()
    while(True):
        state.print_board()
        input(f"Player {state.turn}, please enter your move\n", in_coordinates)
        xy = parse_place(in_coordinates)
        if not xy: 
            continue
        if not state.open_square(xy):
            continue
        state.mark_square(xy)
