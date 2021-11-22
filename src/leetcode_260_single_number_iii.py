# @l2g 260 python3
# [260] Single Number III
# Difficulty: Medium
# https://leetcode.com/problems/single-number-iii
#
# Given an integer array nums,
# in which exactly two elements appear only once and all the other elements appear exactly twice.
# Find the two elements that appear only once.You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
#
# Example 1:
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
# Example 2:
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
# Example 3:
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each integer in nums will appear twice, only two integers will appear once.
#
#

import functools
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # get xor of every elem

        # XOR of single elements
        total_xor = functools.reduce(lambda a, b: a ^ b, nums)

        # One part of bit is different for a, b -> get last 1's position
        last_one = total_xor & (total_xor - 1) ^ total_xor
        nums_with_last_one = [num for num in nums if last_one & num]

        one_of_num = functools.reduce(lambda a, b: a ^ b, nums_with_last_one)

        return [one_of_num, total_xor ^ one_of_num]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_260.py")])
