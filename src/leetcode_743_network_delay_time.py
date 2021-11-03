# @l2g 743 python3
# [743] Network Delay Time
# Difficulty: Medium
# https://leetcode.com/problems/network-delay-time
#
# You are given a network of n nodes,labeled from 1 to n.You are also given times,
# a list of travel times as directed edges times[i] = (ui,vi,wi),where ui is the source node,
# vi is the target node,and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k.
# Return the time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal,return -1.
#
# Example 1:
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
#
# Example 2:
#
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
#
# Example 3:
#
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
#
#
# Constraints:
#
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
#
#

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra
        #         node_map = defaultdict(Counter)
        #         for s, e, t in times:
        #             node_map[s][e] = t

        #         seen = dict()

        #         heap = [[0,k]]
        #         while heap:
        #             cur_time, node = heapq.heappop(heap)
        #             if node not in seen:
        #                 seen[node] = cur_time
        #                 for next_node, td in node_map[node].items():
        #                     heapq.heappush(heap, [cur_time + td, next_node])

        #         return max(seen.values()) if len(seen) == n else -1

        # Short path fast algorithm
        node_map = defaultdict(list)
        for s, e, t in times:
            node_map[s].append([e, t])

        t_arr, q = [0] + [float("inf")] * n, deque()
        q.append([0, k])
        while q:
            time, node = q.popleft()
            if time < t_arr[node]:
                t_arr[node] = time
                for next_node, td in node_map[node]:
                    q.append([time + td, next_node])

        ans = max(t_arr)
        return ans if ans < float("inf") else -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_743.py")])
