from mvc.model.Players import Players
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Game_Rules import Game_Rules

class HumanPlayer(Players):
    def __init__(self, game_piece: Game_Piece):
        super().__init__()
        self.game_piece = game_piece
        self.game_rules = Game_Rules()

    def make_move(self, board: Board, move: tuple):
        """Makes a move on the board

        Args:
            board (Board): The board to make the move on
            move (tuple): The position to make the move on
        """
        move = tuple(map(int, move.split(",")))
        move = move[0] - 1, move[1] - 1
        if self.game_rules.is_valid_move(board, move, self):
            board.set_cell(move[0], move[1], self.game_piece)