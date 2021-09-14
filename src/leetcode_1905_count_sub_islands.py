# @l2g 1905 python3
# [1905] Count Sub Islands
# Difficulty: Medium
# https://leetcode.com/problems/count-sub-islands
#
# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land).
# An island is a group of 1's connected 4-directionally (horizontal or vertical).
# Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.
#
# Example 1:
#
#
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],grid2 = [[1,1,1,0,0],
# [0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are three sub-islands.
#
# Example 2:
#
#
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],grid2 = [[0,0,0,0,0],
# [1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are two sub-islands.
#
#
# Constraints:
#
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
#
#

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])

        def bfs(node):
            q = deque()
            q.append(node)
            in_grid1 = True if grid1[node[0]][node[1]] == 1 else False
            while q:
                node = q.popleft()

                for move in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x, y = node[0] + move[0], node[1] + move[1]
                    if 0 <= x < n and 0 <= y < m and grid2[x][y] == 1:
                        grid2[x][y] = 0

                        q.append((x, y))
                        if grid1[x][y] == 0:
                            in_grid1 = False

            return in_grid1

        def run_bfs():
            islands = 0
            for i in range(n):
                for j in range(m):
                    if grid2[i][j] == 1:
                        grid2[i][j] = 0
                        in_grid1 = bfs((i, j))
                        islands += int(in_grid1)
            return islands

        ans = run_bfs()
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1905.py")])
