from copy import deepcopy

from mvc.model.Players import Players
from mvc.model.Board import Board
from mvc.model.Game_Rules import Game_Rules
from mvc.model.Game_Piece import Game_Piece

class AdvancedAIPlayer(Players):
    def __init__(self, game_piece: Game_Piece, depth: int = 2):
        super().__init__()
        self.game_piece = game_piece
        self.game_rules = Game_Rules()
        self.player_name = "Player2"
        self.depth = depth

    def make_move(self, board: Board, move: tuple):
        best_move = self.choose_move(board)
        board.set_cell(best_move[0], best_move[1], self.game_piece)


    def choose_move(self, board: Board):
        valid_moves = self.game_rules.get_valid_moves(board, self)
        if self.game_rules.is_valid_move(board, move, self):
            for move in valid_moves:
                new_board = deepcopy(board)
                new_board.set_cell(move[0], move[1], self.game_piece)
                board_value = self.minimax(new_board, self.game_piece, Game_Piece.X)
                return board_value
        

    def minimax(self, board: Board, max_player, min_player):
        if self.game_rules.is_game_over(board):
            return self.game_rules.winner

        valid_moves = self.game_rules.get_valid_moves(board, max_player)
        values = []
        for move in valid_moves:
            new_board = deepcopy(board)
            new_board.set_cell(move[0], move[1], max_player)
            board_value = self.minimax(new_board, min_player, max_player)
            values.append(board_value)

        if self is max_player:
            return self.max_value(board, max_player, min_player)
        else:
            return self.min_value(board, max_player, min_player)

    def max_value(self, board, max_player, min_player):
        if self.game_rules.is_game_over(board):
            return self.game_rules.winner
        if self.depth <= 0:
            return "No more moves, the winner is " + self.game_rules.winner
        if self.depth == 1:
            return self.game_rules.evaluate_board(board)
        v = -float("inf")
        for move in self.game_rules.get_valid_moves(board, max_player):
            new_board = deepcopy(board)
            new_board.set_cell(move[0], move[1], max_player)
            v = max(v, self.minimax(new_board, min_player, max_player))
        return v

    def min_value(self, board, max_player, min_player):
        if self.game_rules.is_game_over(board):
            return self.game_rules.winner
        if self.depth == 0:
            return self.game_rules.evaluate_board(board)
        v = float("inf")
        for move in self.game_rules.get_valid_moves(board, min_player):
            new_board = deepcopy(board)
            new_board.set_cell(move[0], move[1], min_player)
            v = min(v, self.minimax(new_board, max_player, min_player))
        return v