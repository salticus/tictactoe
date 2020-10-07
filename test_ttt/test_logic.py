import pytest
from ttt import logic



@pytest.fixture
def board():
    return {(row, column): f"{row},{column}" 
                for row in range(logic.ROWS)
                for column in range(logic.COLUMNS)}

@pytest.fixture
def state():
    return logic.State()


def test_print_board(state):
    state.print_board()


def test_parse_input(state):
    print(state.parse_place("1,2"))


def test_bad_input(state):
    assert state.parse_place("asdf") is None
    assert state.parse_place("1000,1000") is None
    assert state.parse_place("1000") is None


def test_won(state):
    X = logic.PLAYER_X
    Y = logic.PLAYER_Y
    state.board = {
            (0,0): X, (0,1): X, (0,2): X,
            (1,0): X, (1,1): X, (1,2): X,
            (2,0): X, (2,1): X, (2,2): X,
            }
    assert state.has_player_won(X)

    state.board = {
            (0,0): X, (0,1): Y, (0,2): Y,
            (1,0): Y, (1,1): X, (1,2): Y,
            (2,0): Y, (2,1): Y, (2,2): X,
            }
    assert state.has_player_won(X)

    state.board = {
            (0,0): X, (0,1): Y, (0,2): X,
            (1,0): X, (1,1): Y, (1,2): X,
            (2,0): X, (2,1): Y, (2,2): X,
            }
    assert state.has_player_won(Y)

    state.board = {
            (0,0): X, (0,1): X, (0,2): Y,
            (1,0): X, (1,1): Y, (1,2): X,
            (2,0): Y, (2,1): Y, (2,2): X,
            }
    assert state.has_player_won(Y)
    assert not state.game_is_a_draw()


def test_drawn(state):

    X = logic.PLAYER_X
    Y = logic.PLAYER_Y

    state.board = {
            (0,0): X, (0,1): X, (0,2): Y,
            (1,0): Y, (1,1): Y, (1,2): X,
            (2,0): X, (2,1): Y, (2,2): X,
            }
    assert not state.has_player_won(X)
    assert not state.has_player_won(Y)
    assert state.game_is_a_draw()


def test_prompt():
    pass
