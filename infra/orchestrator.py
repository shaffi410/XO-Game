from player import Player
from util import board_sizes
from validator import Validator
from util.symbol_emun import Symbol
from gui.board import Board
import util.user_interactions
import util.board_sizes


class Orchestrator:
    def __init__(
            self,
        player_1: Player = Player(Symbol.X_SYMBOL),
        player_2: Player = Player(Symbol.O_SYMBOL),
        board: Board = Board(board_sizes.MIN_BOARD_SIZE),
    ):
        validator: Validator = Validator(self.board, self.board, self.player_2)


    @property
    def game_loop(self):






