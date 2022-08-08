from abc import ABC, abstractmethod
from ..model.Board import Board

class BoardView(ABC):
    def __init__(self, board: Board) -> None:
        self.board = board

    def welcome_message(self):
        pass

    def display_game_over(self, winner):
        pass

    def draw(self):
        pass