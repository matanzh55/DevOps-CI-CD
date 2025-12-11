import random

# All possible winning lines: rows, columns, diagonals
WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),   # rows
    (0,3,6), (1,4,7), (2,5,8),   # columns
    (0,4,8), (2,4,6)             # diagonals
]

def available_moves(board):
    """
    Returns a list of indices for empty cells on the board.
    Empty cells are represented by "".
    """
    return [i for i, v in enumerate(board) if v == ""]

def find_winning_move(board, player):
    """
    Finds a move that allows 'player' to win.
    If there are two marks of 'player' in a line and one empty,
    returns the index of the empty cell to win/block.
    """
    for a, b, c in WIN_LINES:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and line.count("") == 1:
            if board[a] == "": return a
            if board[b] == "": return b
            if board[c] == "": return c
    return None

def opposite_corner_move(board, opponent='X'):
    """
    If opponent occupies a corner, take the opposite corner if free.
    """
    pairs = [(0,8), (2,6)]
    for p, q in pairs:
        if board[p] == opponent and board[q] == "":
            return q
        if board[q] == opponent and board[p] == "":
            return p
    return None

def bot_move(board, bot='O', opponent='X'):
    """
    Determines the bot's move based on strategy:
    1. Win if possible
    2. Block opponent from winning
    3. Take the center
    4. Take opposite corner
    5. Take a random empty corner
    6. Take a random empty side
    """
    # 1. Win if possible
    move = find_winning_move(board, bot)
    if move is not None:
        return move

    # 2. Block opponent if they are about to win
    move = find_winning_move(board, opponent)
    if move is not None:
        return move

    # 3. Take center if empty
    if board[4] == "":
        return 4

    # 4. Take opposite corner
    move = opposite_corner_move(board, opponent)
    if move is not None:
        return move

    # 5. Take a random empty corner
    corners = [i for i in (0,2,6,8) if board[i] == ""]
    if corners:
        return random.choice(corners)

    # 6. Take a random empty side
    sides = [i for i in (1,3,5,7) if board[i] == ""]
    if sides:
        return random.choice(sides)

    # Fallback: choose any available move
    moves = available_moves(board)
    return random.choice(moves) if moves else None

