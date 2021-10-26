# @l2g 169 python3
# [169] Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element
#
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, major_num = 0, nums[0]
        for i in range(len(nums)):
            if nums[i] == major_num:
                count += 1
            elif count == 0:
                major_num, count = nums[i], 1
            else:
                count -= 1

        return major_num


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_169.py")])
