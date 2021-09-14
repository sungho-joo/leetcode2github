# @l2g 90 python3
# [90] Subsets II
# Difficulty: Medium
# https://leetcode.com/problems/subsets-ii
#
# Given an integer array nums that may contain duplicates,return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#

from typing import Counter, List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)

        ans = []

        def dfs(pos, ans_list):

            key = list(count.keys())[pos]
            for c in range(count[key] + 1):
                if pos == len(count) - 1:
                    ans.append(ans_list + [key] * c)
                else:
                    dfs(pos + 1, ans_list + [key] * c)

        dfs(0, [])
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_90.py")])
