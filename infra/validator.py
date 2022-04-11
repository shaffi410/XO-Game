from gui.board import Board
from infra.player import Player
from util.board_size_enum import BoardSize


class Validator:

    def __init__(
            self,
            board: Board,
            is_game_over: bool,
            player_1: Player,
            player_2: Player,
            board_is_full: bool,
            board_size: int
    ):
        self.board: Board = board
        self.is_game_over: bool = False
        self.player_1: Player = player_1
        self.player_2: Player = player_2
        self.board_is_full = False
        self.board_size: int = 0

    def validate_board_size_input(self, board_size: str) -> bool:
        if board_size != BoardSize.THREE or BoardSize.FIVE or BoardSize.SEVEN or BoardSize.NINE:
            return False
        self.board_size = board_size
        return True

    def validate_player_input(self, player_input_x: int, player_input_y: int) -> bool:
        return

    def _validate_slot_is_empty(self,  player_input_x: int, player_input_y: int )-> bool:
        if self.board[player_input_x][player_input_y] ==

    def _validate_slot_is_in_range(self, player_input_x: int, player_input_y: int)-> bool:
        return

    def validate_game_is_over(self, player_1, player_2) -> bool:
        if player_2.player_won or player_2.player_won or self.board_is_full:
            self.is_game_over = True
            return self.is_game_over
        return self.is_game_over

    def validate_board_is_full(self):
        if self.board.board_occupied_slots == self.board_size:
            return True
        return False

