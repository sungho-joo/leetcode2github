# @l2g 283 python3
# [283] Move Zeroes
# Difficulty: Easy
# https://leetcode.com/problems/move-zeroes
#
# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
# Follow up: Could you minimize the total number of operations done?

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_283.py")])
