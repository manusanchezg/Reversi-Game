from mvc.model.Players import Players
from mvc.model.Board import Board
from mvc.model.Game_Rules import Game_Rules
from mvc.model.Game_Piece import Game_Piece

class AIPlayer(Players):
    def __init__(self, game_piece: Game_Piece):
        super().__init__()
        self.game_piece = game_piece
        self.game_rules = Game_Rules()

    def make_move(self, board, move: tuple):
        pass
        



    def get_valid_moves(self, board: Board, game_rules: Game_Rules, player: Game_Piece.O):
        valid_moves = []
        for i in range(board.size):
            for j in range(board.size):
                if game_rules.is_valid_move(board, (i, j), player):
                    valid_moves.append((i, j))
        return valid_moves

    def get_best_move(self, board: Board, game_rules: Game_Rules, player: Game_Piece.O):
        valid_moves = self.get_valid_moves(board, game_rules, player)
        best_move = -1
        best_score = -1
        for move in valid_moves:
            score = self.get_move_score(board, game_rules, move, player)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def get_move_score(self, board: Board, game_rules: Game_Rules, move: tuple, player: Game_Piece.O):
        board.make_move(move, player)
        if game_rules.is_game_over(board):
            if game_rules.is_winner(board, player):
                return 1
            else:
                return 0
        else:
            return self.get_best_move(board, game_rules, player)