from mvc.model.Board import Board
from mvc.model.Errors import InvalidCoordRangeStepError, InvalidMoveError
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Players import Players

class Game_Rules:
    """ Rules of the game that may be changed in the future
    """
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1),   (-1, -1),  (1, -1),   (-1, 1)]
                #  down    right     up     left   down-right  up-left  down-left   up-right
    
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
            # position in the matrix given by the user
            mat_pos = board.mat[move[0]][move[1]]

            if mat_pos != board.EMPTY_CELL:
                raise InvalidMoveError
            if not (0 <= move[0] < board.size and 0 <= move[1] < board.size):
                raise InvalidCoordRangeStepError

            # check if the move is valid in all directions
            for direction in self.DIRECTIONS:
                if self.check_direction(board, move, direction, player):
                    return True
            raise InvalidMoveError

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
        pieces = {"X": 0, "O": 0}
        if board.is_full():
            for row in board.mat:
                for cell in row:
                    if Game_Piece.X == cell:
                        pieces["X"] += 1
                    else:
                        pieces["O"] += 1
            
            if pieces["X"] == 0:
                print("No X pieces")
                print("Game over, O wins")
            elif pieces["O"] == 0:
                print("No O pieces")
                print("Game over, X wins")
            if pieces["X"] == pieces["O"]:
                print("It's a tie!")
                return True
            elif pieces["X"] > pieces["O"]:
                print("X wins!")
                return True
            else:
                print("O wins!")
                return True
        return False

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
        # checks if there is a piece of the player in the direction
        # (They have to be separated by one or more of the other player pieces)
        while True:
            x += dx
            y += dy
            if not (0 <= x < board.size and 0 <= y < board.size):
                return False
            mat_pos = board.mat[x][y]
            if mat_pos != player.game_piece:
                if mat_pos == board.EMPTY_CELL:
                    return False
                else:
                    # run a loop to check if there is another piece of the player in the direction
                    while True:
                        x += dx
                        y += dy
                        if not (0 <= x < board.size and 0 <= y < board.size):
                            return False
                        mat_pos = board.mat[x][y]
                        if mat_pos == player.game_piece:
                            return True
                        elif mat_pos == board.EMPTY_CELL:
                            return False
                        else:
                            return True

            if mat_pos == player.game_piece:
                return False

    
    def check_flipping(self, board: Board, move: tuple, direction: tuple, player: Players) -> bool:
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
        # checks if there is a piece of the player in the direction
        # (They have to be separated by one or more of the other player pieces)
        while True:
            x += dx
            y += dy
            if not (0 <= x < board.size and 0 <= y < board.size):
                return False
            mat_pos = board.mat[x][y]
            if mat_pos != player.game_piece:
                if mat_pos == board.EMPTY_CELL:
                    return True
                else:
                    # run a loop to check if there is another piece of the player in the direction
                    while True:
                        x += dx
                        y += dy
                        if not (0 <= x < board.size and 0 <= y < board.size):
                            return False
                        mat_pos = board.mat[x][y]
                        if mat_pos == player.game_piece:
                            return True
                        elif mat_pos == board.EMPTY_CELL:
                            return False
                        else:
                            return True

            if mat_pos == player.game_piece:
                return False

    def flip_pieces(self, board: Board, move: tuple, player: Players) -> None:
        """Flips the pieces in a certain direction
        Args:
            board (Board): The board to flip the pieces on
            move (tuple): The move to flip the pieces in
            player (Players): The player to flip the pieces for
        """
        move = tuple(map(int, move.split(",")))
        move = move[0] - 1, move[1] - 1
        for direction in self.DIRECTIONS:
            if self.check_flipping(board, move, direction, player):
                self.flip_pieces_in_direction(board, move, direction, player)
    
    def flip_pieces_in_direction(self, board: Board, move: tuple, direction: tuple, player: Players) -> None:
        """Flips the pieces in a certain direction
        Args:
            board (Board): The board to flip the pieces on
            move (tuple): The move to flip the pieces in
            direction (tuple): The direction to flip the pieces in
            player (Players): The player to flip the pieces for
        """
        x, y = move
        dx, dy = direction
        while True:
            x += dx
            y += dy
            if not (0 <= x < board.size and 0 <= y < board.size):
                break
            mat_pos = board.mat[x][y]
            if mat_pos == player.game_piece:
                continue
            if mat_pos == board.EMPTY_CELL:
                break
            board.flip_game_piece(player.game_piece, (x, y))

