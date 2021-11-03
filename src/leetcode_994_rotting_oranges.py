# @l2g 994 python3
# [994] Rotting Oranges
# Difficulty: Medium
# https://leetcode.com/problems/rotting-oranges
#
# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible,return -1.
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2,column 0) is never rotten,
# because rotting only happens 4-directionally.
#
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        count = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not boundary_checker(nx, ny):
                        continue
                    if grid[nx][ny] == 1:
                        q.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh -= 1
            count += 1
        return count - 1 if fresh == 0 else -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_994.py")])
