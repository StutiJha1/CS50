"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    flat = sum(board, [])
    x_count = flat.count(X)
    o_count = flat.count(O)
    return X if x_count == o_count else O


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Invalid move")
    new_board = deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    if terminal(board):
        return None

    current = player(board)

    def max_value(b):
        if terminal(b):
            return utility(b), None
        v = -math.inf
        best_action = None
        for action in actions(b):
            min_result, _ = min_value(result(b, action))
            if min_result > v:
                v, best_action = min_result, action
        return v, best_action

    def min_value(b):
        if terminal(b):
            return utility(b), None
        v = math.inf
        best_action = None
        for action in actions(b):
            max_result, _ = max_value(result(b, action))
            if max_result < v:
                v, best_action = max_result, action
        return v, best_action

    return max_value(board)[1] if current == X else min_value(board)[1]
