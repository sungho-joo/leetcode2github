# @l2g 240 python3
# [240] Search a 2D Matrix II
# Difficulty: Medium
# https://leetcode.com/problems/search-a-2d-matrix-ii
#
# Write an efficient algorithm that searches for a target value in an m x n integer matrix.
# The matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
# Example 1:
#
#
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
#
# Example 2:
#
#
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
#
#

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        r, c = 0, m - 1

        while r < n and 0 <= c:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_240.py")])
