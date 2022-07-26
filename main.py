from mvc.model.Board import Board
from mvc.controller.controller import StartGame
from mvc.model.Human_Player import HumanPlayer
from mvc.model.Game import Game

board = Board()
game = Game(board, HumanPlayer(), HumanPlayer())

Player1 = HumanPlayer()
Player2 = HumanPlayer()


game = StartGame(board, player1=Player1, player2=Player2, game=game)
game.start()