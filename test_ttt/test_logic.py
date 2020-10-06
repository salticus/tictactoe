import pytest
from ttt import logic



@pytest.fixture
def board():
    return {(row, column): f"{row},{column}" 
                for row in range(logic.ROWS)
                for column in range(logic.COLUMNS)}


def test_print_board(board):
    logic.print_board(board)
