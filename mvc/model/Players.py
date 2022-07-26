from abc import ABC, abstractmethod
from mvc.model.Game_Piece import Game_Piece

class Players(ABC):
    def __init__(self):
        self.game_piece = Game_Piece.X
        self.game_pieces = 2
        pass

    def make_move(self, board, move):
        pass

    def __str__(self) -> str:
        pass