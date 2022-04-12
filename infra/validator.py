from gui.board import Board
from player import Player
from util.symbol_emun import Symbol
from util import board_sizes


class Validator:

    def __init__(
            self,
            board: Board,
            player_1: Player,
            player_2: Player,
    ):
        self.board: Board = board
        self.player_1: Player = player_1
        self.player_2: Player = player_2
        self.is_game_over: bool = False
        self.board_is_full: bool = False

    def validate_board_size_input(self, board_size: str) -> bool:
        if board_size > board_sizes.MAX_BOARD_SIZE:
            return False
        self.board.board_size = board_size
        return True

    def _validate_slot_is_empty(self, player_input_x: int, player_input_y: int) -> bool:
        if self.board.get_slot(player_input_x, player_input_y) == Symbol.EMPTY_SYMBOL:
            return True
        return False

    def _validate_slot_is_in_range(self, player_input_x: int, player_input_y: int) -> bool:
        if player_input_x < self.board.board_size and player_input_y < self.board.board_size:
            return True
        return False

    def validate_player_input(self, player_input_x: int, player_input_y: int) -> bool:
        if self._validate_slot_is_in_range(player_input_x, player_input_x) and self._validate_slot_is_in_range(player_input_x, player_input_y):
            return True

    def validate_game_is_over(self, player_1, player_2) -> bool:
        if player_2.player_won or player_2.player_won or self.board_is_full:
            self.is_game_over = True
            return self.is_game_over
        return self.is_game_over

    def validate_board_is_full(self) -> bool:
        if self.board.board_occupied_slots == self.board_size:
            self.board_is_full = True
            return self.board_is_full
        return self.board_is_full


