# @l2g 200 python3
# [200] Number of Islands
# Difficulty: Medium
# https://leetcode.com/problems/number-of-islands
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(pos):
            q = collections.deque()
            q.append(pos)
            grid[pos[0]][pos[1]] = -1

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if boundary_checker(nx, ny) and grid[nx][ny] == "1":
                        q.append([nx, ny])
                        grid[nx][ny] = -1

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs([i, j])
                    ans += 1
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_200.py")])
