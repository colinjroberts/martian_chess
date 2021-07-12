import pytest
from Game import *

game = Game(["h", "h"])

# Tests for the game
# - moves that eventually end a game
# - try moves on and off the board
# - try moving not your piece, especially near the boundary
# - try promoting when you aren't supposed to
# - try moving pieces outside their usual range
# - try moving pieces incorrectly
# - try moving through pieces
# - capture pieces
# - promote pieces
# - compare final scores


@pytest.mark.parametrize("move,expected", [
    # QUEEN
    ("1bQ2a", ("d", ["b1", "a2"])),  # Queen diagonal up left one
    ("3cQ1a", ("d", ["c3", "b2", "a1"])),  # Queen diagonal down left two
    ("1aQ3c", ("d", ["a1", "b2", "c3"])),  # Queen diagonal up right three
    ("4aQd1", ("d", ["a4", "b3", "c2", "d1"])),  # Queen diagonal down right four
    ("3cQ3a", ("h", ["c3", "b3", "a3"])),  # Queen horizontal left two
    ("8aQd8", ("h", ["a8", "b8", "c8", "d8"])),  # Queen horizontal right four
    ("1aQa6", ("v", ["a1", "a2", "a3", "a4", "a5", "a6"])),  # Queen vertical up six
    ("d8Q1d", ("v", ["d8", "d7", "d6", "d5", "d4", "d3", "d2", "d1"])),  # Queen vertical down eight

])
def test_get_path(move, expected):
    assert game.board.get_path(move) == expected



# check_move_string_length,
# - moves with correct length
# - moves missing part of the move down to 0

# check_move_format
# - "1aQb1", "a1Qb1", "a1Q1b", "1aQ1b" all valid
# - "1ab1Q", "Qa1b1", "Qab11" invalid...maybe try other combos?

# check_move_start_is_not_end,
# - "6aQb6", "a6Qa6", "a6Q6a", "6aQ6a"
# - maybe generate some random test cases?

# check_move_starting_position,
# -

# check_move_destination,
# check_move_path,