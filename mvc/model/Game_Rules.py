from mvc.model.Board import Board
from mvc.model.Game_Piece import Game_Piece
from mvc.model.Players import Players

class Game_Rules:
    """ Rules of the game that may be changed in the future
    """
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1),   (-1, -1),  (1, -1),   (-1, 1)]
                #  down    right     up     left   down-right  up-left  down-left   up-right
    
    def __init__(self) -> None:
        self.winner = None

    def is_valid_move(self, board: Board, move: tuple, player: Players) -> bool:
        """Checks wether the move is valid or not
        Args:
            board (Board): The board to check the move on
            move (tuple): The move to check
        Returns:
            bool: True if the move is valid, False otherwise
        """
        # position in the matrix given by the user
        x, y = move
        if not (0 <= x < board.size and 0 <= y < board.size):
            return False
        mat_pos = board.mat[x][y]

        if mat_pos != board.EMPTY_CELL:
            return False

        # check if the move is valid in all directions
        for direction in self.DIRECTIONS:
            if self.check_direction(board, move, direction, player):
                return True
        return False

    def is_game_over(self, board: Board, player1: Players, player2: Players) -> bool:
        """Checks if there is any space left in the board to keep playing
        Args:
            board (Board): The board to check
        Returns:
            bool: True if there is space left, False otherwise
        """
        pieces = {"X": 0, "O": 0}
        # count the number of pieces in the board
        for row in board.mat:
            for cell in row:
                if Game_Piece.X == cell:
                    pieces["X"] += 1
                elif Game_Piece.O == cell:
                    pieces["O"] += 1

        if board.is_full():    
            if pieces["X"] == pieces["O"]:
                print("It's a tie!")
                return True
            elif pieces["X"] > pieces["O"]:
                self.winner = player1.player_name
                self.get_winner()
                return True
            else:
                self.winner = player2.player_name
                self.get_winner()
                return True
        else:
            if pieces["X"] == 0:
                self.winner = player2.player_name
                self.get_winner()
                return True
            elif pieces["O"] == 0:
                self.winner = player1.player_name
                self.get_winner()
                return True
            elif self.get_valid_moves(board, player1) == []:
                print("No valid moves for X")
                return False
            elif self.get_valid_moves(board, player2) == []:
                print("No valid moves for O")
                return False
            elif self.get_valid_moves(board, player1) == [] and self.get_valid_moves(board, player2) == []:
                print("No valid moves for both players")
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
                    break
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
                            break
                        else:
                            continue

            if mat_pos == player.game_piece:
                return False

    def flip_pieces(self, board: Board, move: tuple, player: Players) -> None:
        """Flips the pieces in a certain direction
        Args:
            board (Board): The board to flip the pieces on
            move (tuple): The move to flip the pieces in
            player (Players): The player to flip the pieces for
        """
        for direction in self.DIRECTIONS:
            if self.check_flipping(board, move, direction, player):
                self.flip_pieces_in_direction(board, move, direction, player)

    
    def check_flipping(self, board: Board, move: tuple, direction: tuple, player: Players) -> bool:
        """Checks if it has to keep flipping pieces
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
                            continue

            if mat_pos == player.game_piece:
                return False
    
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
                break
            if mat_pos == board.EMPTY_CELL:
                break
            board.flip_game_piece(player.game_piece, (x, y))

    def get_valid_moves(self, board: Board, player: Players) -> list:
        """Gets all the valid moves for the player
        Returns:
            list: A list of valid moves
        """
        valid_moves = []
        for x in range(board.size):
            for y in range(board.size):
                if self.is_valid_move(board, (x, y), player):
                    valid_moves.append((x, y))
        return valid_moves

    def get_winner(self) -> Game_Piece:
        """Gets the winner of the game
        Returns:
            Game_Piece: The winner of the game
        """
        return f'No more moves, the winner is {self.winner}'

    def evaluate_board(self, board: Board, player: Players) -> int:
        """Evaluates the board for the player
        Returns:
            int: The evaluation of the board for the player
        """
        return 0