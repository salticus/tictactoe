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
        self.whose_turn = PLAYER_X
        self.status = "Playing"
        self.score = {PLAYER_X: 0, PLAYER_Y: 0}

    def reset(self):
        self.board = self._clear_board()
        self.whose_turn = PLAYER_X
        self.status = "Playing"

    def change_turns(self):
        self.whose_turn = PLAYER_X if self.whose_turn == PLAYER_Y else PLAYER_Y

    def _clear_board(self):
        return {(row, column): BLANK
                for row in range(self.rows)
                    for column in range(self.columns)}

    def open_square(self, xy):
        """
        Verify that the spot is not already taken
        """
        return self.board[xy] == BLANK

    def mark_square(self, xy):
        """
        Mark square.
        Check for win or draw status
        """
        self.board[xy] = self.whose_turn
        self.print_board()
        if self.has_player_won(self.whose_turn):
            print(f"Player {self.whose_turn}, you have won!")
            self.reset()
        if self.game_is_a_draw():
            print(f"This game is a draw. Restarting the game.")
            self.reset()
        self.change_turns()


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

    def game_is_a_draw(self):
        """
        Check for conflict along any line
        """
        both_players = set((PLAYER_X, PLAYER_Y))
        board = self.board

        # check 
        all_rows = all( set(board[(row, v)] for v in range(self.columns)) == both_players
                                for row in range(self.rows) )
        all_columns = all( set(board[(v, column)] for v in range(self.rows)) == both_players
                                for column in range(self.columns) )

        # back slash, assumes square
        back_slash = (set(board[(v, v)] for v in range(self.rows)) == both_players)

        forward_slash_xys = zip(range(self.rows), range(self.columns)[::-1])
        forward_slash = (set(board[xy] for xy in forward_slash_xys) == both_players)

        return all((all_rows, all_columns, back_slash, forward_slash))

    def print_board(self):
        """
        board: {(x: int, y: int): value
        """
        print(end="\n")
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.board[(row, column)], end=" | ")
            print()
            for column in range(self.columns):
                print("-", end="-|-")
            print(end="\n")

    def parse_place(self, string):
        # clean
        try:
            x, y = string.split(",")
            row = int(x.strip())
            column = int(y.strip())
        except ValueError as e:
            print("Coordinates must be a comma separated pair of numbers, column first"
                    "For example: 2, 1\n")
            return None
        if (self.rows <= row) or (self.columns <= column):
            print("Coordinates must be within the space on the board (zero indexed ;-)")
            return None
        return (row, column)

        
    def loop(self):
        """
        Start game
        """
        print("Coordinates are zero based")
        print()
        self.print_board()
        while(True):
            in_xy = input(f"Player {self.whose_turn}, please enter your move\n")
            xy = self.parse_place(in_xy)
            if not xy: 
                continue
            if not self.open_square(xy):
                print("That square is already taken! Try another.")
                continue
            self.mark_square(xy)


if __name__ == "__main__":
    state = State()
    state.loop()
