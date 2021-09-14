# @l2g 827 python3
# [827] Making A Large Island
# Difficulty: Hard
# https://leetcode.com/problems/making-a-large-island
#
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.
#
# Example 1:
#
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#
# Example 2:
#
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:
#
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
#

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        island_area = {0: 0}

        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m

        def bfs(node, island_num):
            q = deque()
            q.append(node)
            grid[node[0]][node[1]] = island_num

            area = 1
            while q:
                x, y = q.popleft()
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    n_x = x + dx
                    n_y = y + dy
                    if boundary_checker(n_x, n_y) and grid[n_x][n_y] == 1:
                        grid[n_x][n_y] = island_num
                        q.append((n_x, n_y))
                        area += 1
            return area

        island_num = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = bfs((i, j), island_num)
                    island_area[island_num] = area
                    island_num += 1

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    total_area = 0
                    island_set = set([0])
                    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        n_x = i + dx
                        n_y = j + dy
                        if boundary_checker(n_x, n_y):
                            island_set.add(grid[n_x][n_y])
                    total_area = sum([island_area[island] for island in island_set]) + 1
                    ans = max(ans, total_area)

        return m * n if ans == 0 else ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_827.py")])
