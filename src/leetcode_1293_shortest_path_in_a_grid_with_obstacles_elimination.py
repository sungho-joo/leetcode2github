# @l2g 1293 python3
# [1293] Shortest Path in a Grid with Obstacles Elimination
# Difficulty: Hard
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination
#
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
# You can move up,down,left,or right from and to an empty cell in one step.
# Return the minimum number of steps to walk from the upper left corner (0,
# 0) to the lower right corner (m - 1,n - 1) given that you can eliminate at most k obstacles.
# If it is not possible to find such walk return -1.
#
# Example 1:
#
#
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation:
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6.Such path is (0,0) -> (0,
# 1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#
# Example 2:
#
#
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
#
#

from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if k >= n + m - 3:
            return n + m - 2

        q = deque()
        q.append((0, 0, k))
        visited = {(0, 0, k)}
        step = 0
        while q:
            for _ in range(len(q)):
                x, y, remaining = q.popleft()
                if x == (n - 1) and y == (m - 1):
                    return step
                # if k >= n-1-x + m-1-y: return step + n-1-x + m-1-y
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if boundary_checker(nx, ny) and (nx, ny, remaining) not in visited:
                        new_k = remaining - grid[nx][ny]
                        if remaining >= 0:
                            q.append((nx, ny, new_k))
                            visited.add((nx, ny, new_k))
            step += 1

        return -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1293.py")])
