# @l2g 130 python3
# [130] Surrounded Regions
# Difficulty: Medium
# https://leetcode.com/problems/surrounded-regions
#
# Given an m x n matrix board containing 'X' and 'O',
# capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example 1:
#
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border,
# which means that any 'O' on the border of the board are not flipped to 'X'.
# Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally or vertically.
#
# Example 2:
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(x, y):
            q = deque()
            q.append([x, y])
            board[x][y] = 0
            region = []
            is_removable = True
            while q:
                cur_x, cur_y = q.popleft()
                region.append([cur_x, cur_y])
                for dx, dy in dirs:
                    nx, ny = cur_x + dx, cur_y + dy
                    if not boundary_checker(nx, ny):
                        is_removable = False
                        continue
                    if board[nx][ny] == "O":
                        q.append([nx, ny])
                        board[nx][ny] = 0
            if is_removable:
                for r_x, r_y in region:
                    board[r_x][r_y] = "X"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    bfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = "O"


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_130.py")])
