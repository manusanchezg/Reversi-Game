from mvc.model.Players import Players
from mvc.model.Board import Board
from mvc.model.Game_Rules import Game_Rules
from mvc.model.Game_Piece import Game_Piece

class AIPlayer(Players):
    def __init__(self, game_piece: Game_Piece):
        super().__init__()
        self.game_piece = game_piece
        self.game_rules = Game_Rules()
        self.player_name = "Player2"

    def make_move(self, board: Board, move: tuple):
        valid_moves = self.get_valid_moves(board, self)
        if self.game_rules.is_valid_move(board, move, self):
            for move in valid_moves:
                new_board = Board(board.mat)
                board_value = self.minimax(new_board, self.game_piece, Game_Piece.X)
                board.set_cell(move[0], move[1], self.game_piece)
                return board_value
        



    def get_valid_moves(self, board: Board, player) -> list:
        """Gets all the valid moves for the AI
        Returns:
            list: contains all the valid moves
        """
        valid_moves = []
        for i in range(board.size):
            for j in range(board.size):
                if self.game_rules.is_valid_move(board, (i, j), player):
                    valid_moves.append((i, j))
        return valid_moves

    def minimax(self, board, max_player, min_player):
        if self.game_rules.is_game_over(board):
            return self.game_rules.winner
        if max_player == Game_Piece.X:
            return self.max_value(board, max_player, min_player)
        else:
            return self.min_value(board, max_player, min_player)