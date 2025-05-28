"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Initial state
    if board == initial_state():
        return X

    # Middle of the game
    x_count, o_count = 0, 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    if i not in range(3) or j not in range(3):
        raise Exception(
            "Invalid move. You are not allowed to play outside the Tic-Tac-Toe box"
        )

    if board[i][j] != EMPTY:
        raise Exception("Invalid move. This cell was already played in.")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    cells = []
    diag1, diag2 = [], []
    for i in range(3):

        cells.append(board[i])
        col = []
        for j in range(3):
            col.append(board[j][i])
            if i == j:
                diag1.append(board[i][j])
        cells.append(col)
    diag2 = [board[0][2], board[1][1], board[2][0]]
    cells.append(diag1)
    cells.append(diag2)

    for cell in cells:
        if cell.count(X) == 3:
            return X
        elif cell.count(O) == 3:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Game over and win
    if winner(board) is not None:
        return True

    # Tie
    filled = True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                # In progress
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    # Minimax algorithm with alpha-beta prunning
    optimal_move = (None, None)
    optimal_utility = float("-inf") if player(board) == X else float("inf")

    possible_actions = actions(board)
    alpha, beta = float("-inf"), float("inf")
    for action in possible_actions:

        if player(board) == X:
            utility_value = min_value((result(board, action)), alpha, beta)
            if optimal_utility < utility_value:
                optimal_utility = utility_value
                optimal_move = action

        else:
            utility_value = max_value((result(board, action)), alpha, beta)
            if optimal_utility > utility_value:
                optimal_utility = utility_value
                optimal_move = action

    return optimal_move


def max_value(board, alpha, beta):
    """
    Returns a utility value
    """
    if terminal(board):
        return utility(board)

    v = float("-inf")
    possible_actions = actions(board)
    for action in possible_actions:
        v = max(v, min_value(result(board, action), alpha, beta))

        # X considering O's moves: sees a child move larger than or equal to O's current minimum and we decide O would optimally never play this so we prune the leaf.
        if v >= beta:
            return v
        alpha = max(alpha, v)

    return v


def min_value(board, alpha, beta):
    """
    Returns a utility value
    """

    if terminal(board):
        return utility(board)

    v = float("inf")
    possible_actions = actions(board)
    for action in possible_actions:
        v = min(v, max_value(result(board, action), alpha, beta))

        # O considering X's moves: sees a child move less than or equal to 0's current maximum and we decide X would optimally never play this so we prune this leaf.
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
