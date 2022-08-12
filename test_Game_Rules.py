import unittest
from mvc.model.Game_Rules import Game_Rules
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Human_Player import HumanPlayer


class TestGameRules(unittest.TestCase):
    def setUp(self):
        self.game_rules = Game_Rules()
        self.board = Board()
        self.player = HumanPlayer(Game_Piece.X)
        self.player2 = HumanPlayer(Game_Piece.O)
        self.board.set_cell(3, 4, Game_Piece.X)
        self.board.set_cell(4, 3, Game_Piece.X)
        self.board.set_cell(3, 3, Game_Piece.O)
        self.board.set_cell(4, 4, Game_Piece.O)

    def test_is_valid_move(self):
        self.setUp()
        self.assertFalse(self.game_rules.is_valid_move(self.board, (0, 0), self.player))
        self.assertTrue(self.game_rules.is_valid_move(self.board, (4, 5), self.player))
        self.assertFalse(self.game_rules.is_valid_move(self.board, (4, 5), self.player2))
        self.assertTrue(self.game_rules.is_valid_move(self.board, (3, 5), self.player2))

    
    def test_is_game_over(self):
        self.setUp()
        self.assertFalse(self.game_rules.is_game_over(self.board))
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.set_cell(i, j, Game_Piece.X)
        self.assertTrue(self.game_rules.is_game_over(self.board))
        self.assertTrue(self.game_rules.winner == Game_Piece.X)

    def test_flip_pieces(self):
        self.setUp()
        self.game_rules.flip_pieces(self.board, (4, 5), self.player)
        self.assertFalse(self.board.get_cell(4, 4) == Game_Piece.O)
        self.assertTrue(self.board.get_cell(3, 3) == Game_Piece.O)
        self.assertTrue(self.board.get_cell(4, 4) == Game_Piece.X)