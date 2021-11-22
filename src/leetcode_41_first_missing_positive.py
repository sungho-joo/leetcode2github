# @l2g 41 python3
# [41] First Missing Positive
# Difficulty: Hard
# https://leetcode.com/problems/first-missing-positive
#
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
#
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        for i in range(n):
            if nums[i] > 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1

        for i in range(slow):
            if 0 < abs(nums[i]) <= slow and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        for i in range(slow):
            if nums[i] > 0:
                return i + 1
        return slow + 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_41.py")])
