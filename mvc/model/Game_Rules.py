from mvc.model.Board import Board
from mvc.model.Errors import InvalidCoordRangeStepError, InvalidMoveError
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Players import Players

class Game_Rules:
    """ Rules of the game that may be changed in the future
    """
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def __init__(self) -> None:
        pass

    def is_valid_move(self, board: Board, move: tuple, player: Players) -> bool:
        """Checks wether the move is valid or not
        Args:
            board (Board): The board to check the move on
            move (tuple): The move to check
        Returns:
            bool: True if the move is valid, False otherwise
        """
        try:
            mat_pos = board.mat[move[0]][move[1]]
            if mat_pos != board.EMPTY_CELL:
                raise InvalidMoveError
            if not (0 <= move[0] < board.size and 0 <= move[1] < board.size):
                raise InvalidCoordRangeStepError
            for direction in self.DIRECTIONS:
                if self.check_direction(board, move, direction, player):
                    return True
            raise InvalidMoveError
            # return board.mat[move[0]][move[1]] == Board.EMPTY_CELL
        except InvalidCoordRangeStepError:
            print()
            print("Move out of range!")
            print()
        except InvalidMoveError:
            print()
            print("Invalid move!")
            print()

    def is_game_over(self, board: Board) -> bool:
        """Checks if there is any space left in the board to keep playing
        Args:
            board (Board): The board to check
        Returns:
            bool: True if there is space left, False otherwise
        """
        return board.is_full()
    
    def check_direction(self, board: Board, move: tuple, direction: tuple, player: Players) -> bool:
        """Checks if the move is valid in a certain direction
        Args:
            board (Board): The board to check the move on
            move (tuple): The move to check
            direction (tuple): The direction to check
        Returns:
            bool: True if the move is valid, False otherwise
        """
        x, y = move
        dx, dy = direction
        while True:
            x += dx
            y += dy
            if not (0 <= x < board.size and 0 <= y < board.size):
                return False
            mat_pos = board.mat[x][y]
            if mat_pos == player.game_piece:
                return True
            if mat_pos != player.game_piece:
                if mat_pos == board.EMPTY_CELL:
                    return False
                else:
                    continue