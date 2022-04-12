import board_sizes

user_interactions = dict(
    choose_board_size=f"please choose a board size from {board_sizes.MIN_BOARD_SIZE} to {board_sizes.MAX_BOARD_SIZE}",
    invalid_board_size="Sorry the number you have entered is not valid",
    choose_board_slot="please choose a valid slot",
    slot_is_taken="Sorry, Slot is taken",
    invalid_slot="no such slot exists",
    game_over_player_1_won="YIIPII KA YAIII!!!!!\n - Player 1 Has Won!! ",
    game_over_player_2_won="YIIPII KA YAIII!!!!!\n - Player 2 Has Won!! ",
    game_over_draw="Oh No! Its  A Draw!",
    play_again="You wish to play again?"
)
