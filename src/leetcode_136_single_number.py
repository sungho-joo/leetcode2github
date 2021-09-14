# @l2g 136 python3
# [136] Single Number
# Difficulty: Easy
# https://leetcode.com/problems/single-number
#
# Given a non-empty array of integers nums,every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears only once.
#
#

import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for i, v in count.items():
            if v == 1:
                return i


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_136.py")])
