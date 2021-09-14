# @l2g 1761 python3
# [1761] Minimum Degree of a Connected Trio in a Graph
# Difficulty: Hard
# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph
#
# You are given an undirected graph.
# You are given an integer n which is the number of nodes in the graph and an array edges,
# where each edges[i] = [ui,vi] indicates that there is an undirected edge between ui and vi.
# A connected trio is a set of three nodes where there is an edge between every pair of them.
# The degree of a connected trio is the number of edges where one endpoint is in the trio,
# and the other is not.
# Return the minimum degree of a connected trio in the graph,
# or -1 if the graph has no connected trios.
#
# Example 1:
#
#
# Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# Output: 3
# Explanation: There is exactly one trio,which is [1,2,3].
# The edges that form its degree are bolded in the figure above.
#
# Example 2:
#
#
# Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# Output: 0
# Explanation: There are exactly three trios:
# 1) [1,4,3] with degree 0.
# 2) [2,5,6] with degree 2.
# 3) [5,6,7] with degree 2.
#
#
# Constraints:
#
# 2 <= n <= 400
# edges[i].length == 2
# 1 <= edges.length <= n * (n-1) / 2
# 1 <= ui, vi <= n
# ui != vi
# There are no repeated edges.
#
#

from typing import DefaultDict, List, Set


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:

        connect_map: DefaultDict[int, Set[int]] = defaultdict(set)
        max_num = n ** 2
        self.min_degree = max_num

        for edge in edges:
            connect_map[edge[0]].add(edge[1])
            connect_map[edge[1]].add(edge[0])

        len_list = {i: len(connect_map[i]) for i in connect_map}

        for n in connect_map:
            for m in connect_map[n]:
                for o in connect_map[n] & connect_map[m]:
                    degree = len_list[n] + len_list[m] + len_list[o] - 6
                    self.min_degree = min(degree, self.min_degree)
                    if n in connect_map[o]:
                        connect_map[o].remove(n)
                if n in connect_map[m]:
                    connect_map[m].remove(n)

        if self.min_degree == max_num:
            self.min_degree = -1
        return self.min_degree


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1761.py")])
