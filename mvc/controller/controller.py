from mvc.model.Game_Rules import Game_Rules
from mvc.view.board_console_view import BoardConsoleView
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Human_Player import HumanPlayer
from mvc.model.AI import AIPlayer

class StartGame:
    def __init__(self, board: Board, player1: HumanPlayer, game_rules: Game_Rules):
        self.board = board
        self.player1 = player1
        self.current_player = self.player1
        self.game_rules = game_rules

    def start(self):
        # set the board to it's initial state
        self.board.set_cell(3, 4, Game_Piece.X)
        self.board.set_cell(4, 3, Game_Piece.X)
        self.board.set_cell(4, 4, Game_Piece.O)
        self.board.set_cell(3, 3, Game_Piece.O)

        # The player choose if they want to play against a computer or another player
        # Player 1 is always human
        player = BoardConsoleView(self.board).display_choose_player()
        if player == "1":
            self.player2 = HumanPlayer(Game_Piece.O)
        if player == "2":
            self.player2 = AIPlayer(Game_Piece.O)

        while True:
            # not very scalable, but it works
            if not self.game_rules.is_game_over(self.board):
                player = self.current_player.player_name
                BoardConsoleView(self.board).draw()

                if type(self.current_player) != AIPlayer:
                    move = input(f"{player}, make your move (row, col): ")
                    move = tuple(map(int, move.split(",")))
                    move = move[0] - 1, move[1] - 1
                    # while the move is not valid, ask for a new move
                    while not self.game_rules.is_valid_move(self.board, move, self.current_player):
                        move = input(f"{player}, make your move (row, col): ")
                        move = tuple(map(int, move.split(",")))
                        move = move[0] - 1, move[1] - 1

                self.current_player.make_move(self.board, move)
                self.game_rules.flip_pieces(self.board, move, self.current_player)
                self.change_players()

    def change_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1 
                

        