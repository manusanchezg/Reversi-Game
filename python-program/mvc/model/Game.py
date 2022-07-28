from mvc.model.Game_Rules import Game_Rules
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece

class Game:
    def __init__(self, board: Board, player1, player2, AI = False):
        self.board = board
        self.player1 = player1
        self.current_player = player1
        if AI:
            self.player2 = AI
        else: 
            self.player2 = player2

    def change_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1 