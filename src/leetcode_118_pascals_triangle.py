# @l2g 118 python3
# [118] Pascal's Triangle
# Difficulty: Easy
# https://leetcode.com/problems/pascals-triangle
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= numRows <= 30
#
#

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * (i + 1) for i in range(numRows)]

        for row in range(numRows - 1):
            for j in range(row):
                ans[row + 1][j + 1] = ans[row][j] + ans[row][j + 1]
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_118.py")])
