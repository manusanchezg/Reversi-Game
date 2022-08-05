from copy import deepcopy
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
        board.set_cell(move[0], move[1], self.game_piece)

    def get_best_move(self, board: Board, player: Players) -> tuple:
        """Gets the best move for the AI
        Returns:
            tuple: the best move for the AI
        """
        valid_moves = self.game_rules.get_valid_moves(board, player)
        best_move = None
        best_score = -1000
        new_board = deepcopy(board)
        for move in valid_moves:
            new_board.set_cell(move[0], move[1], player.game_piece)
            self.game_rules.flip_pieces(new_board, move, player)
            score = self.get_score(new_board, player)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def get_score(self, board: Board, player: Players) -> int:
        """Gets the score for the AI
        Returns:
            int: the score of the AI
        """
        score = 0
        for i in range(board.size):
            for j in range(board.size):
                if board.get_cell(i, j) == player.game_piece:
                    score += 1
                elif board.get_cell(i, j) == Game_Piece.X:
                    score -= 1
        return score
