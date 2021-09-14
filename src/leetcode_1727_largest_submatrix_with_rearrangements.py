# @l2g 1727 python3
# [1727] Largest Submatrix With Rearrangements
# Difficulty: Medium
# https://leetcode.com/problems/largest-submatrix-with-rearrangements
#
# You are given a binary matrix matrix of size m x n,
# and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
#
# Example 1:
#
#
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
#
# Example 2:
#
#
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
#
# Example 3:
#
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns,
# and there is no way to make a submatrix of 1s larger than an area of 2.
# Example 4:
#
# Input: matrix = [[0,0],[0,0]]
# Output: 0
# Explanation: As there are no 1s, no submatrix of 1s can be formed and the area is 0.
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 10^5
# matrix[i][j] is 0 or 1.
#
#

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # count_consecutive_ones = [[0] * n for _ in range(m)]

        # Column-wise loop
        for column_ind in range(n):
            temp_sum = 0
            for row_ind in range(m):
                if matrix[row_ind][column_ind] == 1:
                    temp_sum += 1
                    matrix[row_ind][column_ind] = temp_sum
                else:
                    temp_sum = 0

        def get_max_area_for_row(sorted_row):
            row_max_area = 0
            for i, height in enumerate(sorted_row):
                if height == 0:
                    break
                row_max_area = max(row_max_area, height * (i + 1))
            return row_max_area

        max_area = 0
        for row in matrix:
            row.sort(reverse=True)
            row_max_area = get_max_area_for_row(row)
            max_area = max(max_area, row_max_area)

        return max_area


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1727.py")])
