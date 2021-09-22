# @l2g 54 python3
# [54] Spiral Matrix
# Difficulty: Medium
# https://leetcode.com/problems/spiral-matrix
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m
        ans = []
        dir_key, x, y = 0, 0, -1
        while len(ans) < (n * m):
            nx, ny = x + direction[dir_key][0], y + direction[dir_key][1]
            if boundary_checker(nx, ny) and matrix[nx][ny] != 101:
                ans.append(matrix[nx][ny])
                matrix[nx][ny] = 101
                x, y = nx, ny
            else:
                dir_key = (dir_key + 1) % 4

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_54.py")])
