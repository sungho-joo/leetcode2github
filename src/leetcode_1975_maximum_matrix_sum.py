# @l2g 1975 python3
# [1975] Maximum Matrix Sum
# Difficulty: Medium
# https://leetcode.com/problems/maximum-matrix-sum
#
# You are given an n x n integer matrix. You can do the following operation any number of times:
#
# Choose any two adjacent elements of matrix and multiply each of them by -1.
#
# Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements.
# Return the maximum sum of the matrix's elements using the operation mentioned above.
#
# Example 1:
#
#
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
#
# Example 2:
#
#
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -10^5 <= matrix[i][j] <= 10^5
#
#

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        negative_nums = 0
        min_num = float("inf")
        abs_total = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negative_nums += 1
                min_num = min(min_num, abs(matrix[i][j]))
                abs_total += abs(matrix[i][j])

        return abs_total if negative_nums % 2 == 0 else abs_total - 2 * min_num


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1975.py")])
