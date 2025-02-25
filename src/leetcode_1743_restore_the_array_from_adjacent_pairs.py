# @l2g 1743 python3
# [1743] Restore the Array From Adjacent Pairs
# Difficulty: Medium
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs
#
# There is an integer array nums that consists of n unique elements,but you have forgotten it.However,
# you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui,
# vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs,
# either as [nums[i],nums[i+1]] or [nums[i+1],nums[i]].The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.
#
# Example 1:
#
# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
#
# Example 2:
#
# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
#
# Example 3:
#
# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]
#
#
# Constraints:
#
# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 10^5
# -10^5 <= nums[i], ui, vi <= 10^5
# There exists some nums that has adjacentPairs as its pairs.
#
#

from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pair_counter = defaultdict(list)

        for pair in adjacentPairs:
            pair_counter[pair[0]].append(pair)
            pair_counter[pair[1]].append(pair[::-1])

        single_node = set([node for node, value in pair_counter.items() if len(value) == 1])

        ans = []
        while len(single_node) != 0:
            start_node = single_node.pop()
            ans.append(start_node)
            link = pair_counter[start_node][0]

            pairs = pair_counter[link[1]]
            while len(pairs) != 1:
                pair_counter[link[1]].remove(link[::-1])
                link = pairs[0]
                ans.append(link[0])
                pairs = pair_counter[link[1]]

            ans.append(link[1])
            single_node.remove(link[1])

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1743.py")])
