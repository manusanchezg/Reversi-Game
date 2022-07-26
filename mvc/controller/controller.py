from mvc.model.Players import Players
from mvc.view.board_console_view import BoardConsoleView
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Human_Player import HumanPlayer
from mvc.model.Game import Game

class StartGame:
    def __init__(self, board: Board, player1: HumanPlayer, player2: Players, game: Game):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.winner = None
        self.game_over = False
        self.game_pieces = 2
        self.game = game

    def start(self):
        self.board.set_cell(3, 4, Game_Piece.X)
        self.board.set_cell(4, 3, Game_Piece.X)
        self.board.set_cell(4, 4, Game_Piece.O)
        self.board.set_cell(3, 3, Game_Piece.O)
        while True:
            BoardConsoleView(self.board).draw()
            move = input("Player 1, make your move (row, col): ")
            self.player1.make_move(self.board, move)
            self.game.change_players()

        