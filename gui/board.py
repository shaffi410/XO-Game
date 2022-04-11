import numpy as np

from util.symbol_emun import Symbol


class Board:

    def __init__(
            self,
            board_size: int,
    ):

        self.board_size: int = board_size
        self.board: np = np.zeros(shape=(self.board_size, self.board_size), dtype=int)
        self.board_occupied_slots: int = 0

    def enter_symbol(self, symbol: Symbol, player_input_x: int, player_input_y: int):
        self.board[player_input_x][player_input_y].append(symbol)
        self.board_occupied_slots += 1

    def print_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print("|", end="")
                if j == self.board_size - 1:
                    print(f"{self.board[i][j]}|", end="\n")
                else:
                    print(f"{self.board[i][j]}|", end="")
            if i < self.board_size - 1:
                for k in range(self.board_size * 2 + 1):
                    print("_", end="")
                    if k == self.board_size * 2:
                        print("_", end="\n")



