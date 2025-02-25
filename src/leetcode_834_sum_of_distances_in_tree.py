# @l2g 834 python3
# [834] Sum of Distances in Tree
# Difficulty: Hard
# https://leetcode.com/problems/sum-of-distances-in-tree
#
# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given the integer n and the array edges where edges[i] = [ai,
# bi] indicates that there is an edge between nodes ai and bi in the tree.
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
#
# Example 1:
#
#
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
#
# Example 2:
#
#
# Input: n = 1, edges = []
# Output: [0]
#
# Example 3:
#
#
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
#
#
# Constraints:
#
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
#
#

import collections
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # DP state : node, DP value : reachable nodes' distance map DP transition : node transition
        node_map = collections.defaultdict(list)
        for a, b in edges:
            node_map[a].append(b)
            node_map[b].append(a)

        count = [0] * n
        sum_dist = [0] * n

        def dfs1(node, prev):
            cnt, dist = 1, 0
            for next_node in node_map[node]:
                if next_node != prev:
                    next_cnt, next_dist = dfs1(next_node, node)
                    cnt += next_cnt
                    dist += next_dist + next_cnt
            count[node] = cnt
            sum_dist[node] = dist

            return cnt, dist

        def dfs2(node, prev):
            for next_node in node_map[node]:
                if next_node != prev:
                    sum_dist[next_node] = sum_dist[node] + (len(node_map) - 2 * count[next_node])
                    dfs2(next_node, node)

        # Assume root is 0
        total_cnt, total_dist = dfs1(0, -1)
        dfs2(0, -1)

        if n == 1:
            return [0]

        return sum_dist


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_834.py")])
