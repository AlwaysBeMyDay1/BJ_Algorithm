# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 안전지대


# sol.2
# numpy로 pad 해주
import numpy as np
from collections import Counter

def solution(board):
    result_board = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    board = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    for i_x, x in enumerate(board):
        for i_y, y in enumerate(x):
            if y == 1:
                for ni_x in range(i_x - 1, i_x+2):
                    for ni_y in range(i_y - 1, i_y+2):
                        result_board[ni_x][ni_y] = 1
    print(result_board)

    danger_list = result_board.reshape(1, -1).squeeze()
    answer = Counter(danger_list)[0]
    return answer

# sol.2
# numpy로 pad 해주
import numpy as np

def solution2(board):
    result_board = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    board = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    for i_x, x in enumerate(board):
        for i_y, y in enumerate(x):
            if y == 1:
                result_board[i_x - 1][i_y - 1] = 1
                result_board[i_x - 1][i_y] = 1
                result_board[i_x - 1][i_y + 1] = 1
                result_board[i_x][i_y - 1] = 1
                result_board[i_x][i_y + 1] = 1
                result_board[i_x + 1][i_y - 1] = 1
                result_board[i_x + 1][i_y] = 1
                result_board[i_x + 1][i_y + 1] = 1
    print(result_board)

    count = 0
    for x in result_board:
        for y in x:
            if y == 0:
                count += 1
    return count

# sol.1
from copy import deepcopy

def solution1(board):
    result_board = deepcopy(board)
    for i_x, x in enumerate(board):
        for i_y, y in enumerate(x):
            if y == 1:
                print(board)
                try:
                    result_board[i_x - 1][i_y - 1] = 1
                    result_board[i_x - 1][i_y] = 1
                    result_board[i_x - 1][i_y + 1] = 1
                    result_board[i_x][i_y - 1] = 1
                    result_board[i_x][i_y + 1] = 1
                    result_board[i_x + 1][i_y - 1] = 1
                    result_board[i_x + 1][i_y] = 1
                    result_board[i_x + 1][i_y + 1] = 1
                except:
                    pass
                print(board)
    print(result_board)

    count = 0
    for x in result_board:
        for y in x:
            if y == 0:
                count += 1
    return count


print(
    solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]))
