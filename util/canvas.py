import numpy as np
from util.symbol_emun import Symbol


class Canvas:

    def __init__(
            self,
            canvas_size: int,
    ):

        self.canvas_size: int = canvas_size
        self.board: np = np.arange("-").reshape(self.canvas_size, self.canvas_size)
        self.board_occupied_slots: int = 0

    def enter_symbol(self, symbol: Symbol, player_input_x: int, player_input_y: int):
        self.board[player_input_x][player_input_y].append(symbol)
        self.board_occupied_slots += 1

    def print_canvas(self):
        for i in range(self.canvas_size - 1):
            for j in range(self.canvas_size - 1):
                print("|")
                print(self.board[i][j] + "|")
                if j == self.canvas_size - 1:
                    print(self.board[i][j] + "|", end="\n")
            for _ in range(self.canvas_size*2 + 1):
                print("_")

