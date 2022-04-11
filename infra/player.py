from util.symbol_emun import Symbol
from gui.board import Board

class Player:

    def __init__(
            self,
            player_symbol: Symbol
    ):
        self.is_playing: bool = False
        self.player_won: bool = False
        self.player_symbol: Symbol = player_symbol


    def enter_symbol(self, board: Board):
        return






