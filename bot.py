# bot.py
import random
from typing import Optional, List

def bot_move(board: List[str]) -> Optional[int]:
    """
    Choose a move for O.
    board: list of 9 strings: "", "X", or "O".
    returns index (0..8) or None if no move possible.
    """
    available = [i for i, v in enumerate(board) if v == ""]
    if not available:
        return None
    return random.choice(available)
