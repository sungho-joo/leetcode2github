# @l2g 37 python3
# [37] Sudoku Solver
# Difficulty: Hard
# https://leetcode.com/problems/sudoku-solver
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
# The '.' character indicates empty cells.
#
# Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".",
# "9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",
# ".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".",
# "4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8",
# "3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9",
# "1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4",
# "1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
#
#
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
#
#

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_checker = lambda num, r: num in set(board[r])
        col_checker = lambda num, c: num in set([board[i][c] for i in range(9)])

        box_coord = lambda r, c: (3 * (r // 3), 3 * (c // 3))
        box_num_getter = lambda box_x, box_y: [
            board[box_x + x][box_y + y] for x in range(3) for y in range(3)
        ]

        def box_checker(num, r, c):
            box_x, box_y = box_coord(r, c)
            box_nums = box_num_getter(box_x, box_y)
            return num in set(box_nums)

        def get_next_pos(x, y):
            if x == 9:
                return (-1, -1)
            if board[x][y] == ".":
                return (x, y)
            if board[x][y] != ".":
                return get_next_pos(x + (y + 1) // 9, (y + 1) % 9)

        def dfs(num, pos):
            # print(pos)
            if pos[0] == 9:
                return True

            if row_checker(num, pos[0]):
                return False
            if col_checker(num, pos[1]):
                return False
            if box_checker(num, pos[0], pos[1]):
                return False

            board[pos[0]][pos[1]] = num
            next_pos = get_next_pos(*pos)
            if next_pos[0] == -1:
                return True

            for next_num in range(1, 10):
                if dfs(str(next_num), next_pos):
                    return True

            board[pos[0]][pos[1]] = "."
            return False

        initial_pos = get_next_pos(0, 0)
        for i in range(1, 10):
            dfs(str(i), initial_pos)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_37.py")])
