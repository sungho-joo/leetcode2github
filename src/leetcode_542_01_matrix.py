# @l2g 542 python3
# [542] 01 Matrix
# Difficulty: Medium
# https://leetcode.com/problems/01-matrix
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
#
# Example 1:
#
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
# Example 2:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
#
#

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        canvas = [[-1] * m for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    canvas[i][j] = 0
                    q.append((i, j))

        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m

        while q:
            x, y = q.popleft()
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                n_x, n_y = x + dx, y + dy
                if boundary_checker(n_x, n_y) and canvas[n_x][n_y] == -1:
                    canvas[n_x][n_y] = canvas[x][y] + 1
                    q.append((n_x, n_y))

        return canvas


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_542.py")])
