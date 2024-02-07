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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nb=0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is not None :
                nb+=1
    if nb%2 :
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is None :
                actionsSet.add((i,j))
    return actionsSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    newB = copy.deepcopy(board)
    newB[i][j]=player(board)
    return newB


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] is not None:
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] is not None:
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and board[2][2]is not None:
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[2][0] is not None:
        return board[1][1]
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if len(actions(board))==0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    if winner(board)==O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move



def max_val(board):
    if terminal(board):
        return utility(board),  None
    v=-3
    move=None
    for action in actions(board):
        tmp,act=min_val(result(board,action))
        if tmp>v:
            v=tmp
            move=action
    return v, move

def min_val(board):
    if terminal(board):
        return utility(board), None
    v=3
    move=None
    for action in actions(board):
        tmp,act=max_val(result(board,action))
        if tmp<v:
            v=tmp
            move=action
    return v, move