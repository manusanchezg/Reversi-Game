from mvc.model.Game_Piece import Game_Piece

class Board:
    """The board of the game. Can be any size (NxN), the default size is 8*8
    """
    EMPTY_CELL = 0

    def __init__(self, size = 8):
        self.size = size

        # Create a board of the given size with empty cells
        self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]

    def get_cell(self, row, col):
        """Get the value of a cell
        """
        return self.mat[row][col]

    def set_cell(self, row, col, player):
        """Set the value of a cell (X or O)
        """
        self.mat[row][col] = player
    
    def is_full(self):
        """Check if the board is full
        """
        for row in self.mat:
            for cell in row:
                if cell == self.EMPTY_CELL:
                    return False
        return True

    def flip_game_piece(self, game_piece, move: tuple):
        x, y = move
        if game_piece != Game_Piece.X:
            self.set_cell(x, y, Game_Piece.O)
        else:
            self.set_cell(x, y, Game_Piece.X)

    # Just for testing
    def __str__(self):
        """Print the board
        """
        s = ""
        for row in self.mat:
            for cell in row:
                s += str(cell)
            s += "\n"
        return s
    