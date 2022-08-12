from mvc.model.Game_Rules import Game_Rules
from mvc.view.board_console_view import BoardConsoleView
from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Human_Player import HumanPlayer
from mvc.model.AI import AIPlayer
from mvc.model.Advanced_AI import AdvancedAIPlayer

class StartGame:
    def __init__(self, board: Board, player1: HumanPlayer, game_rules: Game_Rules):
        self.board = board
        self.player1 = player1
        self.current_player = self.player1
        self.game_rules = game_rules

    def start(self):
        # set the board to it's initial state
        middle = self.board.size // 2
        self.board.set_cell(middle - 1, middle, Game_Piece.X)
        self.board.set_cell(middle, middle - 1, Game_Piece.X)
        self.board.set_cell(middle, middle, Game_Piece.O)
        self.board.set_cell(middle - 1, middle - 1, Game_Piece.O)

        # The player choose if they want to play against a computer or another player
        # Player 1 is always human
        player = BoardConsoleView(self.board).display_choose_player()
        if player == "1":
            self.player2 = HumanPlayer(Game_Piece.O)
        if player == "2":
            self.player2 = AIPlayer(Game_Piece.O)
        if player == "3":
            choice = BoardConsoleView(self.board).display_choose_difficulty()
            self.player2 = AdvancedAIPlayer(Game_Piece.O, choice)

        while True:
            # infinite loops that ends when the game is over
            BoardConsoleView(self.board).draw()
            if not self.game_rules.is_game_over(self.board, self.player1, self.player2) and \
             self.game_rules.get_valid_moves(self.board, self.current_player):
                player = self.current_player.player_name

                # if type(self.current_player) != AIPlayer:
                if isinstance(self.current_player, HumanPlayer):
                    move = input(f"{player}, make your move (row, col): ")
                    move = tuple(map(int, move.split(",")))
                    move = move[0] - 1, move[1] - 1
                    # while the move is not valid, ask for a new move
                    while not self.game_rules.is_valid_move(self.board, move, self.current_player):
                        print("Invalid move, please try again")
                        move = input(f"{player}, make your move (row, col): ")
                        move = tuple(map(int, move.split(",")))
                        move = move[0] - 1, move[1] - 1

                    self.current_player.make_move(self.board, move)
                    self.game_rules.flip_pieces(self.board, move, self.current_player)
                    self.change_players()
                    
                else:
                    move = self.current_player.get_best_move(self.board, self.current_player)
                    self.current_player.make_move(self.board, move)
                    self.game_rules.flip_pieces(self.board, move, self.current_player)
                    self.change_players()

            else:
                print(self.game_rules.get_winner())
                break

    def change_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1 
                

        