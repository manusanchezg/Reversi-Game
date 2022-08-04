from mvc.model.Board import Board
from mvc.controller.controller import StartGame
from mvc.model.Human_Player import HumanPlayer
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Game_Rules import Game_Rules

Player1 = HumanPlayer(Game_Piece.X)
game_rules = Game_Rules()
board = Board()



game = StartGame(board, player1=Player1, game_rules=game_rules)
game.start()