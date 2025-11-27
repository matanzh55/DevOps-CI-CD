# tests/test_game_logic.py
import pytest
from game_logic import TicTacToe

def test_make_valid_moves_and_winner_row():
    g = TicTacToe()
    assert g.make_move(0, "X")
    assert g.make_move(3, "O")
    assert g.make_move(1, "X")
    assert g.make_move(4, "O")
    assert g.make_move(2, "X")  # X completes top row
    assert g.winner == "X"

def test_invalid_move_rejected():
    g = TicTacToe()
    assert g.make_move(0, "X")
    assert not g.make_move(0, "O")  # cannot override

def test_draw_detection():
    g = TicTacToe()
    moves = [
        (0,"X"),(1,"O"),(2,"X"),
        (4,"O"),(3,"X"),(5,"O"),
        (7,"X"),(6,"O"),(8,"X")
    ]
    for pos, p in moves:
        assert g.make_move(pos, p)
    assert g.winner == "Draw"
