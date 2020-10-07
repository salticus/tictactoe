# CLI Python Tic Tac Toe

- A way for each player to take their turn and enter their move
- Only valid moves are allowed
- Detect when one player has won
- Detect when there is a tie
- Show the current game board
- Show the current score

Note: "the current score" implies the game restarts when it is done (won or drawn)


# Set Up

Requires Python 3.6

    git clone https://github.com/salticus/tictactoe
    pushd tictactoe
    # or python -m ttt
    # python -v will show what
    python3 -m ttt


# Testing

    # install dependencies
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -U pip
    pip install -r requirements
  
    # run tests
    python -m pytest

    # run tests, not capturing output
    python -m pytest -s

    # run subset of tests, e.g. test_bad_input
    python -m pytest -k bad
