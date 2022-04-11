from player import Player
from validator import Validator
from util.symbol_emun import Symbol
from gui.board import Board
import util.user_interactions

class Orchestrator:

    def __init__(self):
        player_1: Player = Player(Symbol.X_SYMBOL)
        player_2 = Player(Symbol.O_SYMBOL)
        board = util.user_interactions[]