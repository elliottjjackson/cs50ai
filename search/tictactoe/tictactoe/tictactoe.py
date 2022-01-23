"""
Tic Tac Toe Player
"""

from ast import Pass
from cmath import inf
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    X_count = sum([row.count(X) for row in board])
    O_count = sum([row.count(O) for row in board])
    return X if (O_count == X_count) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    return set(
        (i, j)
        for i, row in enumerate(board)
        for j, cell in enumerate(row)
        if board[i][j] is EMPTY
    )


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    # raise NotImplementedError
    cell = board[i][j]
    current_player = player(board)
    if cell == EMPTY:
        board_copy = deepcopy(board)
        board_copy[i][j] = current_player
    else:
        raise RuntimeError(
            f"{current_player} is unable to play in cell {(i,j)}."
            f"{cell} has already played there."
        )
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    def horizontal_winner(player, board):
        for row in board:
            if row.count(player) == 3:
                return player
        return None

    def vertical_winner(player, board):
        width = len(board[0])
        columns = []
        for j in range(width):
            columns.append([row[j] for row in board])
        for column in columns:
            if column.count(player) == 3:
                return player
        return None

    def diagonal_winner(player, board):
        diagonals = []
        length = len(board)
        diagonals.append([board[i][i] for i in range(length)])
        diagonals.append([board[i][length - 1 - i] for i in range(length)])
        for diagonal in diagonals:
            if diagonal.count(player) == 3:
                return player
        return None

    for player in [O, X]:
        winner = horizontal_winner(player, board)
        if winner == player:
            return winner
        winner = vertical_winner(player, board)
        if winner == player:
            return winner
        winner = diagonal_winner(player, board)
        if winner == player:
            return winner
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif all([all(cells) for cells in board]):  # tie condition
        return True
    else:  # Game is still progressing
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    evaluation_dictionary = {}

    if terminal(board):
        return None

    def max_value(board, parent_action):
        v = -inf
        if terminal(board):
            if parent_action not in evaluation_dictionary:
                evaluation_dictionary[parent_action] = []
                evaluation_dictionary[parent_action].append(utility(board))
            return utility(board)
        else:
            for action in actions(board):
                v_new = min_value(result(board, action), parent_action)
                v = max(v, v_new)
            return v

    def min_value(board, parent_action):
        v = inf
        if terminal(board):
            if parent_action not in evaluation_dictionary:
                evaluation_dictionary[parent_action] = []
                evaluation_dictionary[parent_action].append(utility(board))
            return utility(board)
        else:
            for action in actions(board):
                v_new = max_value(result(board, action), parent_action)
                v = min(v, v_new)
            return v

    action_list = list(actions(board))

    if player(board) == X:
        for action in action_list:
            max_value(board, action)
    elif player(board) == O:
        for action in action_list:
            min_value(board, action)
    else:
        return None

    print(evaluation_dictionary)

    # if player(board) == X:
    #     utility_list = [max_value(result(board, action)) for action in action_list]
    #     for i, uti in enumerate(utility_list):
    #         if uti == 1:
    #             return action_list[i]
    #     for i, uti in enumerate(utility_list):
    #         if uti == 0:
    #             return action_list[i]
    #     return action_list[0]

    # if player(board) == O:
    #     utility_list = [min_value(result(board, action)) for action in action_list]
    #     for i, uti in enumerate(utility_list):
    #         if uti == -1:
    #             return action_list[i]
    #     for i, uti in enumerate(utility_list):
    #         if uti == 0:
    #             return action_list[i]
    #     return action_list[0]


board = [
    [X, O, EMPTY],
    [X, EMPTY, X],
    [O, X, O],
]

minimax(board)
