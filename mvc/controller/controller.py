from mvc.model.Game_Rules import Game_Rules
from mvc.model.Players import Players
from mvc.view.board_console_view import BoardConsoleView
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Human_Player import HumanPlayer
from mvc.model.Game import Game

class StartGame:
    def __init__(self, board: Board, player1: HumanPlayer, player2: Players, game: Game, game_rules: Game_Rules):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.game_rules = game_rules

    def start(self):
        self.board.set_cell(3, 4, Game_Piece.X)
        self.board.set_cell(4, 3, Game_Piece.X)
        self.board.set_cell(4, 4, Game_Piece.O)
        self.board.set_cell(3, 3, Game_Piece.O)
        while True:
            # not very scalable, but it works
            if not self.game_rules.is_game_over(self.board):
                player = self.current_player.player_name
                BoardConsoleView(self.board).draw()
                move = input(f"{player}, make your move (row, col): ")
                self.game_rules.flip_pieces(self.board, move, self.current_player)
                self.change_players()

    def change_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1 
                

        