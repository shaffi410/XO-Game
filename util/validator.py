from canvas import Canvas
from player import Player
from util.board_size_enum import BoardSize


class Validator:

    def __init__(
            self,
            canvas: Canvas,
            is_game_over: bool,
            player_1: Player,
            player_2: Player,
            canvas_is_full: bool,
            canvas_size: int
    ):
        self.canvas: Canvas = canvas
        self.is_game_over: bool = False
        self.player_1: Player = player_1
        self.player_2: Player = player_2
        self.canvas_is_full = False
        self.canvas_size: int = 0

    def validate_canvas_size_input(self, canvas_size: str) -> bool:
        if canvas_size != BoardSize.THREE or BoardSize.FIVE or BoardSize.SEVEN or BoardSize.NINE:
            return False
        self.canvas_size = canvas_size
        return True

    def validate_player_input(self, player_input_x: int, player_input_y: int) -> bool:
        return

    def validate_game_is_over(self, player_1, player_2) -> bool:
        if player_2.player_won or player_2.player_won or self.canvas_is_full:
            self.is_game_over = True
            return self.is_game_over
        return self.is_game_over

    def validate_board_is_full(self):
        if self.canvas.board_occupied_slots == self.canvas_size:
            return True
        return False
