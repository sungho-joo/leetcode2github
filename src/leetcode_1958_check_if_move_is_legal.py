# @l2g 1958 python3
# [1958] Check if Move is Legal
# Difficulty: Medium
# https://leetcode.com/problems/check-if-move-is-legal
#
# You are given a 0-indexed 8 x 8 grid board,where board[r][c] represents the cell (r,
# c) on a game board.On the board,free cells are represented by '.',
# white cells are represented by 'W',and black cells are represented by 'B'.
# Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black).
# However,a move is only legal if,after changing it,
# the cell becomes the endpoint of a good line (horizontal,vertical,or diagonal).
# A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color,
# and the remaining cells in the middle are the opposite color (no cells in the line are free).
# You can find examples for good lines in the figure below:
#
# Given two integers rMove and cMove and a character color representing the color you are playing as (white or black),
# return true if changing cell (rMove,cMove) to color color is a legal move,
# or false if it is not legal.
#
# Example 1:
#
#
# Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".",
# "W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".
# ","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]],
# rMove = 4,cMove = 3,color = "B"
# Output: true
# Explanation: '.','W',and 'B' are represented by the colors blue,white,and black respectively,
# and cell (rMove,cMove) is marked with an 'X'.
# The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
#
# Example 2:
#
#
# Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".
# ",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",
# ".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]],rMove = 4,
# cMove = 4,color = "W"
# Output: false
# Explanation: While there are good lines with the chosen cell as a middle cell,
# there are no good lines with the chosen cell as an endpoint.
#
#
# Constraints:
#
# board.length == board[r].length == 8
# 0 <= rMove, cMove < 8
# board[rMove][cMove] == '.'
# color is either 'B' or 'W'.
#
#

from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        boundary_checker = lambda x, y: 0 <= x < 8 and 0 <= y < 8
        get_next_pos = lambda x, y, cur_dir: (x + cur_dir[0], y + cur_dir[1])

        def check_good_line(x, y, cur_dir, start_color):
            opposite_color = {"B": "W", "W": "B"}
            n_x, n_y = get_next_pos(x, y, cur_dir)
            length = 1
            while boundary_checker(n_x, n_y):
                if board[n_x][n_y] == ".":
                    return False
                if board[n_x][n_y] == opposite_color[start_color]:
                    length += 1
                if board[n_x][n_y] == start_color:
                    return True if length > 1 else False
                n_x, n_y = get_next_pos(n_x, n_y, cur_dir)
            return False

        for cur_dir in directions:
            if check_good_line(rMove, cMove, cur_dir, color):
                return True

        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1958.py")])
