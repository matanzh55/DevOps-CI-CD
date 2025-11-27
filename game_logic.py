# game_logic.py
class TicTacToe:
    def __init__(self):
        self.board = [""] * 9         # 0..8 single-d array representing 3x3
        self.current_player = "X"     # X = human, O = bot
        self.winner = None            # "X", "O", "Draw", or None

    def is_valid_move(self, pos: int) -> bool:
        return isinstance(pos, int) and 0 <= pos < 9 and self.board[pos] == ""

    def make_move(self, pos: int, player: str) -> bool:
        """Place player ('X' or 'O') at pos. Return True if placed, False if invalid."""
        if not self.is_valid_move(pos):
            return False
        self.board[pos] = player
        self.current_player = "O" if player == "X" else "X"
        self.check_winner()
        return True

    def check_winner(self):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],   # rows
            [0,3,6],[1,4,7],[2,5,8],   # cols
            [0,4,8],[2,4,6]            # diags
        ]
        for a, b, c in wins:
            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.board[a]
                return
        if "" not in self.board:
            self.winner = "Draw"
