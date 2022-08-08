import unittest

from mvc.model.Game_Rules import Game_Rules
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Human_Player import HumanPlayer
from mvc.model.AI import AIPlayer

class TestAI(unittest):
    def setUp(self):
        self.game_rules = Game_Rules()
        self.player = HumanPlayer(Game_Piece.X)
        self.player2 = AIPlayer(Game_Piece.O)
        self.board.set_cell(3, 4, Game_Piece.X)
        self.board.set_cell(4, 3, Game_Piece.X)
        self.board.set_cell(3, 3, Game_Piece.O)
        self.board.set_cell(4, 4, Game_Piece.O)

    def test_get_valid_moves(self, board: Board, player: AIPlayer):
        self.setUp()
        self.assertTrue(self.game_rules.get_valid_moves(board, player) == [(4, 5), (5, 4), (5, 5)])
        self.assertTrue(self.game_rules.get_valid_moves(board, player) == [(4, 5), (5, 4), (5, 5)])
        self.assertTrue(self.game_rules.get_valid_moves(board, player) == [(4, 5), (5, 4), (5, 5)])
        self.assertTrue(self.game_rules.get_valid_moves(board, player) == [(4, 5), (5, 4), (5, 5)])
        self.assertTrue(self.game_rules.get_valid_moves(board, player) == [(4, 5), (5, 4), (5, 5)])

