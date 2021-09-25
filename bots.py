import random
from game_functions import *
import random

def my_bot(board, current_player):
    """

    :param board: list with all board elements representing the current game state
    :param current_player: string indicating the current player (either PLAYER_X or PLAYER_O)
    :return: number between 0 and 8 indicating the chosen move
    """

    # TODO create your own bot that is able to beat the random bot
    # Hint: You maybe want to use some of the functions you see imported in line 3.
    # We did not cover imports in the lecture, for now you just have to know that you can simply call them here
    # e.g get_valid_moves(board) returns a list with all valid moves

    # TODO return the chosen move your bot thinks is the best
    return 0


def random_bot(board, current_player):
    """
    Bot that selects a random valid move
    :param board: list with all board elements representing the current game state
    :param current_player: string indicating the current player (either PLAYER_X or PLAYER_O)
    :return: number between 0 and 8 indicating a random (valid) move
    """

    # get all valid moves in the current board state
    valid_moves = get_valid_moves(board)

    # return a random move
    return random.choice(valid_moves)
