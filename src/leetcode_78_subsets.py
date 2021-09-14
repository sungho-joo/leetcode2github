# @l2g 78 python3
# [78] Subsets
# Difficulty: Medium
# https://leetcode.com/problems/subsets
#
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(pos, path):
            ans.append(path)
            if pos == len(nums) - 1:
                return

            for next_pos in range(pos + 1, len(nums)):
                dfs(next_pos, path + [nums[next_pos]])

        dfs(-1, [])
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_78.py")])
