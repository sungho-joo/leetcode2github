# @l2g 1916 python3
# [1916] Count Ways to Build Rooms in an Ant Colony
# Difficulty: Hard
# https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony
#
# You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony.
# You are given the expansion plan as a 0-indexed integer array of length n,prevRoom,
# where prevRoom[i] indicates that you must build room prevRoom[i] before building room i,
# and these two rooms must be connected directly.Room 0 is already built,so prevRoom[0] = -1.
# The expansion plan is given such that once all the rooms are built,
# every room will be reachable from room 0.
# You can only build one room at a time,
# and you can travel freely between rooms you have already built only if they are connected.
# You can choose to build any room as long as its previous room is already built.
# Return the number of different orders you can build all the rooms in.Since the answer may be large,
# return it modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: prevRoom = [-1,0,1]
# Output: 1
# Explanation: There is only one way to build the additional rooms: 0 → 1 → 2
#
# Example 2:
#
#
# Input: prevRoom = [-1,0,0,1,2]
# Output: 6
# Explanation:
# The 6 ways are:
# 0 → 1 → 3 → 2 → 4
# 0 → 2 → 4 → 1 → 3
# 0 → 1 → 2 → 3 → 4
# 0 → 1 → 2 → 4 → 3
# 0 → 2 → 1 → 3 → 4
# 0 → 2 → 1 → 4 → 3
#
#
# Constraints:
#
# n == prevRoom.length
# 2 <= n <= 10^5
# prevRoom[0] == -1
# 0 <= prevRoom[i] < n for all 1 <= i < n
# Every room is reachable from room 0 once all the rooms are built.
#

from typing import List


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        node_map = defaultdict(list)
        for i, prev_node in enumerate(prevRoom):
            node_map[prev_node].append(i)

        # get_comb_num = lambda total, node_num: factorial(total) // (factorial(node_num) * factorial(total - node_num))

        def dp(node):
            if not node_map.get(node):
                return 1, 1

            comb_nums = []
            comb_path = []
            for next_node in node_map[node]:
                num_nodes, paths = dp(next_node)
                comb_nums.append(num_nodes)
                comb_path.append(paths)

            total = sum(comb_nums)
            ans = 1
            for i in range(len(comb_nums)):
                ans *= comb(total, comb_nums[i])
                total -= comb_nums[i]

            return sum(comb_nums) + 1, ans * reduce(lambda x, y: x * y, comb_path) % (10 ** 9 + 7)

        total_nodes, total_paths = dp(-1)
        return total_paths % (10 ** 9 + 7)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1916.py")])
