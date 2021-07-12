from Board import *
import pytest

board = Board(["h", "h"])

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

    # DRONE
    ("b1D1a", ("h", ["b1", "a1"])),  # Drone horizontal left one
    ("c8D8d", ("h", ["c8", "d8"])),  # Drone horizontal right one
    ("d6D5d", ("v", ["d6", "d5"])),  # Drone vertical down one
    ("b2D3b", ("v", ["b2", "b3"])),  # Drone vertical up one
    ("c1D1a", ("h", ["c1", "b1", "a1"])),  # Drone horizontal left two
    ("b8D8d", ("h", ["b8", "c8", "d8"])),  # Drone horizontal right two
    ("d6D4d", ("v", ["d6", "d5", "d4"])),  # Drone vertical down two
    ("b2D4b", ("v", ["b2", "b3", "b4"])),  # Drone vertical up two

    # PAWN
    ("2bQa3", ("d", ["b2", "a3"])),  # Pawn diagonal up left one
    ("2bQa1", ("d", ["b2", "a1"])),  # Pawn diagonal down left one
    ("3cQd4", ("d", ["c3", "d4"])),  # Pawn diagonal up right one
    ("3cQd2", ("d", ["c3", "d2"])),  # Pawn diagonal down right one
])
def test_get_path(move, expected):
    assert board.get_path(move) == expected

# These should all be checked somehow I guess the move will still return a path even if it is invalid
# @pytest.mark.parametrize("move,expected", [
#     # DRONE
#     ("1bQ2a", ("d", ["b1", "a2"])),  # Drone diagonal up left one
#     ("3cQ1a", ("d", ["c3", "b2", "a1"])),  # Drone diagonal down left two
#     ("1aQ3c", ("d", ["a1", "b2", "c3"])),  # Drone diagonal up right three
#     ("4aQd1", ("d", ["a4", "b3", "c2", "d1"])),  # Drone diagonal down right four
#     # Drone horizontal left three
#     # Drone horizontal right four
#     # Drone vertical up three
#     # Drone vertical down two
#
#     # PAWN
#     ("3cQ1a", ("d", ["c3", "b2", "a1"])),  # Pawn diagonal down two
#     ("1aQ3c", ("d", ["a1", "b2", "c3"])),  # Pawn diagonal up two
# #])
# def test_get_path(move, expected):
#     assert board.get_path(move) == expected
