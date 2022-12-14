from ..view.board_view import BoardView
from ..model.Board import Board

class BoardConsoleView(BoardView):
    symbols = {0: " ", 1: "X", 2: "O"}

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def draw(self):
        board_size = self.board.size
        numbers = [str(i) for i in range(1, board_size + 1)]
        header = "-+" + "---+" * (board_size)
        for number in numbers:
            print(" |", number, end="")
        print(" |")
        print(header)
        for i in range(board_size):
            print(numbers[i], end="")
            for j in range(board_size):
                cell = self.board.get_cell(i, j)
                print(f"| {self.symbols[cell]} ", end="")
            print("|")
        print(header)

    def display_game_over(self, winner):
        super().display_game_over()
        print(f"The winner is {winner}")

    def display_choose_player(self):
        print("Please choose a player:")
        print("1. Human Player")
        print("2. Computer Player (easy)")
        print("3. Computer Player (hard)")
        choice = input("Your choice: ")
        return choice

    def display_choose_difficulty(self):
        print("Please choose a difficulty (the higher the number, the higher the diffculty): ")
        choice = input("Your choice: ")
        return choice