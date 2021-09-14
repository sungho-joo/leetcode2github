# @l2g 1914 python3
# [1914] Cyclically Rotating a Grid
# Difficulty: Medium
# https://leetcode.com/problems/cyclically-rotating-a-grid
#
# You are given an m x n integer matrix grid​​​,where m and n are both even integers,and an integer k.
# The matrix is composed of several layers,which is shown in the below image,
# where each color is its own layer:
#
# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix.
# To cyclically rotate a layer once,
# each element in the layer will take the place of the adjacent element in the counter-clockwise direction.
# An example rotation is shown below:
#
# Return the matrix after applying k cyclic rotations to it.
#
# Example 1:
#
#
# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.
#
# Example 2:
#
#
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 10^9
#

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        def rotate_one(outer_grid):
            l, w = len(outer_grid), len(outer_grid[0])
            target = [[0] * w for _ in range(l)]

            # Top
            for i in range(1, w):
                target[0][i - 1] = outer_grid[0][i]

            # Bottom
            for i in range(0, w - 1):
                target[-1][i + 1] = outer_grid[-1][i]

            # Left
            for i in range(0, l - 1):
                target[i + 1][0] = outer_grid[i][0]

            # Right
            for i in range(1, l):
                target[i - 1][-1] = outer_grid[i][-1]

            return target

        smaller_side = min(m, n)
        ans = [[0] * m for _ in range(n)]

        for dec in range(smaller_side // 2):
            outer_grid = []
            for i in range(dec, n - dec):
                outer_grid.append(grid[i][dec : m - dec])
            total_len = 2 * (n - 2 * dec) + 2 * (m - 2 * dec) - 4
            for _ in range(k % total_len):
                outer_grid = rotate_one(outer_grid)
            for i in range(dec, n - dec):
                ans[i][dec : m - dec] = outer_grid[i - dec]

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1914.py")])
