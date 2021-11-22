# @l2g 684 python3
# [684] Redundant Connection
# Difficulty: Medium
# https://leetcode.com/problems/redundant-connection
#
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n,
# with one additional edge added.The added edge has two different vertices chosen from 1 to n,
# and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai,
# bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers,return the answer that occurs last in the input.
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
# Constraints:
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
#
#

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.data = list(range(n + 1))

            def find(self, a):
                if self.data[a] != a:
                    self.data[a] = self.find(self.data[a])
                return self.data[a]

            def union(self, a, b):
                a, b = self.find(a), self.find(b)

                if a != b:
                    self.data[a] = b

        n = len(edges)
        dsu = DSU(n)

        for s, e in edges:
            s_parent = dsu.find(s)
            e_parent = dsu.find(e)
            if s_parent != e_parent:
                dsu.union(*sorted([s, e]))
            else:
                return [s, e]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_684.py")])
