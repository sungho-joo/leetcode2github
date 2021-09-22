# @l2g 15 python3
# [15] 3Sum
# Difficulty: Medium
# https://leetcode.com/problems/3sum
#
# Given an integer array nums,return all the triplets [nums[i],nums[j],nums[k]] such that i != j,
# i != k,and j != k,and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # find -nums[i]
            num_dict = {}
            for j in range(i + 1, n):
                if nums[j] in num_dict:
                    ans.add((nums[i], -nums[i] - nums[j], nums[j]))
                else:
                    num_dict[-nums[i] - nums[j]] = 1

        return map(list, ans)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_15.py")])
