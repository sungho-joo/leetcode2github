# @l2g 1970 python3
# [1970] Last Day Where You Can Still Cross
# Difficulty: Hard
# https://leetcode.com/problems/last-day-where-you-can-still-cross
#
# There is a 1-based binary matrix where 0 represents land and 1 represents water.
# You are given integers row and col representing the number of rows and columns in the matrix,
# respectively.
# Initially on day 0,the entire matrix is land.However,each day a new cell becomes flooded with water.
# You are given a 1-based 2D array cells,where cells[i] = [ri,ci] represents that on the ith day,
# the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e.,
# changed to 1).
# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells.
# You can start from any cell in the top row and end at any cell in the bottom row.
# You can only travel in the four cardinal directions (left,right,up,and down).
# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
#
# Example 1:
#
#
# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
#
# Example 2:
#
#
# Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# Output: 1
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 1.
#
# Example 3:
#
#
# Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# Output: 3
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 3.
#
#
# Constraints:
#
# 2 <= row, col <= 2 * 10^4
# 4 <= row * col <= 2 * 10^4
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# All the values of cells are unique.
#
#

from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self._data = list(range(n))
                self.left_most = [i % col for i in range(n)]
                self.right_most = [i % col for i in range(n)]

            def find(self, a):
                if a != self._data[a]:
                    self._data[a] = self.find(self._data[a])
                return self._data[a]

            def union(self, a, b):
                a, b = self.find(a), self.find(b)

                if a == b:
                    return
                self._data[a] = b
                self.left_most[b] = min(self.left_most[a], self.left_most[b])
                self.right_most[b] = max(self.right_most[a], self.right_most[b])

        # INitialization
        temp_matrix = [[0] * col for _ in range(row)]
        dsu = DSU(row * col)
        directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        # Helper functions
        get_index = lambda x, y: x * col + y
        boundary_checker = lambda x, y: 0 <= x < row and 0 <= y < col

        for ind, cell in enumerate(cells):
            x, y = cell[0] - 1, cell[1] - 1
            temp_matrix[x][y] = 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if boundary_checker(nx, ny) and temp_matrix[nx][ny] == 1:
                    dsu.union(get_index(x, y), get_index(nx, ny))
                    current_root = dsu.find(get_index(x, y))
                    if dsu.left_most[current_root] == 0 and dsu.right_most[current_root] == (col - 1):
                        return ind
        return row * col


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1970.py")])
