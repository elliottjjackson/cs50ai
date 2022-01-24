from tictactoe.tictactoe import player
from tictactoe.tictactoe import actions
from tictactoe.tictactoe import result
from tictactoe.tictactoe import winner
from tictactoe.tictactoe import terminal
from tictactoe.tictactoe import utility
from tictactoe.tictactoe import minimax

X = "X"
O = "O"
EMPTY = None

######## player ############


def test_player_empty_board():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert player(board) == X


def test_player_Os_turn():
    board = [
        [EMPTY, X, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert player(board) == O


def test_player_Os_turn_on_terminal_board():
    board = [
        [O, X, X],
        [X, O, O],
        [X, O, X],
    ]
    assert player(board) == O


######## actions ############


def test_actions_for_9_actions():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert len(actions(board)) == 9


def test_actions_for_8_actions():
    board = [
        [X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert len(actions(board)) == 8


def test_actions_for_7_actions():
    board = [
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [X, EMPTY, EMPTY],
    ]
    assert len(actions(board)) == 7


def test_actions_for_0_actions():
    board = [
        [X, O, X],
        [O, O, X],
        [X, X, O],
    ]
    assert len(actions(board)) == 0


######## result ############


def test_result_on_empty_board_selecting_coord_0_0():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    action = (0, 0)
    assert result(board, action) == [
        [X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


def test_result_on_turn_two_selecting_coord_1_1():
    board = [
        [X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    action = (1, 1)
    assert result(board, action) == [
        [X, EMPTY, EMPTY],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


def test_result_on_turn_three_selecting_coord_1_2():
    board = [
        [X, EMPTY, EMPTY],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    action = (1, 2)
    assert result(board, action) == [
        [X, EMPTY, EMPTY],
        [EMPTY, O, X],
        [EMPTY, EMPTY, EMPTY],
    ]


def test_result_for_invalid_action_where_a_player_already_exists():
    board = [
        [X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    action = (0, 0)
    assert RuntimeError


def test_result_return_board_is_a_copy_of_function_argument_board():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    action = (1, 2)
    assert result(board, action) != board


######## winner ############


def test_winner_for_X_horizontal_win_with_empties():
    board = [
        [X, X, X],
        [EMPTY, EMPTY, EMPTY],
        [O, EMPTY, O],
    ]
    assert winner(board) == X


def test_winner_for_X_vertical_win_with_empties():
    board = [
        [EMPTY, X, EMPTY],
        [EMPTY, X, EMPTY],
        [O, X, O],
    ]
    assert winner(board) == X


def test_winner_for_X_diagonal_win_with_empties():
    board = [
        [X, EMPTY, EMPTY],
        [EMPTY, X, EMPTY],
        [O, O, X],
    ]
    assert winner(board) == X


def test_winner_for_O_horizontal_win_with_empties():
    board = [
        [X, X, EMPTY],
        [O, O, O],
        [EMPTY, X, EMPTY],
    ]
    assert winner(board) == O


def test_winner_for_O_vertical_win_with_empties():
    board = [
        [O, X, EMPTY],
        [O, X, EMPTY],
        [O, EMPTY, X],
    ]
    assert winner(board) == O


def test_winner_for_O_diagonal_win_with_empties():
    board = [
        [X, EMPTY, O],
        [X, O, EMPTY],
        [O, EMPTY, X],
    ]
    assert winner(board) == O


def test_winner_returns_none_for_game_in_progress():
    board = [
        [X, EMPTY, O],
        [X, EMPTY, EMPTY],
        [O, EMPTY, X],
    ]
    assert winner(board) == None


def test_winner_returns_none_for_tie():
    board = [
        [X, X, O],
        [O, X, X],
        [X, O, O],
    ]
    assert winner(board) == None


######## terminal ############


def test_terminal_returns_true_if_the_board_has_a_winner():
    board = [
        [X, EMPTY, O],
        [X, O, EMPTY],
        [O, EMPTY, X],
    ]
    assert terminal(board) == True


def test_terminal_returns_true_if_the_board_is_a_tie():
    board = [
        [X, X, O],
        [O, X, X],
        [X, O, O],
    ]
    assert terminal(board) == True


def test_terminal_returns_false_if_the_board_is_in_progress():
    board = [
        [X, X, O],
        [O, X, X],
        [EMPTY, O, O],
    ]
    assert terminal(board) == False


######## utility ############


def test_utility_identifies_X_as_winner():
    board = [
        [X, X, X],
        [EMPTY, EMPTY, EMPTY],
        [O, EMPTY, O],
    ]
    assert utility(board) == 1


def test_utility_identifies_O_as_winner():
    board = [
        [X, EMPTY, O],
        [X, O, EMPTY],
        [O, EMPTY, X],
    ]
    assert utility(board) == -1


def test_utility_returns_0_for_empty_board():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert utility(board) == 0


def test_utility_returns_0_for_tie():
    board = [
        [X, X, O],
        [O, X, X],
        [X, O, O],
    ]
    assert utility(board) == 0


def test_utility_returns_0_for_board_in_progress():
    board = [
        [X, X, O],
        [O, X, X],
        [EMPTY, O, O],
    ]
    assert utility(board) == 0


######## minimax ############


def test_minimax_takes_last_move():
    board = [
        [X, X, O],
        [O, X, X],
        [EMPTY, O, O],
    ]
    assert minimax(board) == (2, 0)


def test_minimax_suggests_O_blocks_X_diagonal_win():
    board = [
        [X, X, O],
        [O, X, X],
        [EMPTY, O, EMPTY],
    ]
    assert minimax(board) == (2, 2)


def test_minimax_suggests_O_blocks_X_horizontal_win():
    board = [
        [EMPTY, X, O],
        [EMPTY, X, X],
        [EMPTY, O, EMPTY],
    ]
    assert minimax(board) == (1, 0)


def test_minimax_suggests_O_blocks_X_vertical_win():
    board = [
        [EMPTY, X, O],
        [EMPTY, X, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert minimax(board) == (2, 1)


def test_minimax_suggests_X_blocks_O_diagonal_win():
    board = [
        [X, X, O],
        [EMPTY, O, X],
        [EMPTY, O, EMPTY],
    ]
    assert minimax(board) == (2, 0)


def test_minimax_suggests_X_blocks_O_horizontal_win():
    board = [
        [X, EMPTY, EMPTY],
        [O, O, EMPTY],
        [X, EMPTY, EMPTY],
    ]
    assert minimax(board) == (1, 2)


def test_minimax_suggests_X_blocks_O_vertical_win():
    board = [
        [X, O, X],
        [O, O, X],
        [EMPTY, EMPTY, O],
    ]
    assert minimax(board) == (2, 1)


def test_minimax_preferences_X_win_over_O_block():
    board = [
        [X, X, EMPTY],
        [O, O, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert minimax(board) == (0, 2)


def test_minimax_preferences_O_win_over_X_block():
    board = [
        [X, O, X],
        [EMPTY, O, X],
        [EMPTY, EMPTY, EMPTY],
    ]
    assert minimax(board) == (2, 1)
