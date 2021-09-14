# @l2g 1992 python3
# [1992] Find All Groups of Farmland
# Difficulty: Medium
# https://leetcode.com/problems/find-all-groups-of-farmland
#
# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
# To keep the land organized,
# there are designated rectangular areas of hectares that consist entirely of farmland.
# These rectangular areas are called groups.No two groups are adjacent,
# meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
# land can be represented by a coordinate system where the top left corner of land is (0,
# 0) and the bottom right corner of land is (m-1,n-1).
# Find the coordinates of the top left and bottom right corner of each group of farmland.
# A group of farmland with a top left corner at (r1,c1) and a bottom right corner at (r2,
# c2) is represented by the 4-length array [r1,c1,r2,c2].
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land.
# If there are no groups of farmland,return an empty array.You may return the answer in any order.
#
# Example 1:
#
#
# Input: land = [[1,0,0],[0,1,1],[0,1,1]]
# Output: [[0,0,0,0],[1,1,2,2]]
# Explanation:
# The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
# The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
#
# Example 2:
#
#
# Input: land = [[1,1],[1,1]]
# Output: [[0,0,1,1]]
# Explanation:
# The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
#
# Example 3:
#
#
# Input: land = [[0]]
# Output: []
# Explanation:
# There are no groups of farmland.
#
#
# Constraints:
#
# m == land.length
# n == land[i].length
# 1 <= m, n <= 300
# land consists of only 0's and 1's.
# Groups of farmland are rectangular in shape.
#
#

import collections
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        # BFS update land
        is_map = lambda x, y: 0 <= x < n and 0 <= y < m
        directions = [[1, 0], [0, 1]]

        def bfs(pos):
            q = collections.deque()
            q.append(pos)
            land[pos[0]][pos[1]] = 0
            ans = [pos[0], pos[1]]
            last_node = pos[:]
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_map(nx, ny) and land[nx][ny] == 1:
                        q.append([nx, ny])
                        land[nx][ny] = 0
                        last_node = max(last_node, [nx, ny])
            ans.extend(last_node)
            return ans

        ret = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    ret.append(bfs([i, j]))

        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1992.py")])
