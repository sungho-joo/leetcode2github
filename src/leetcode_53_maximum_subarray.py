# @l2g 53 python3
# [53] Maximum Subarray
# Difficulty: Easy
# https://leetcode.com/problems/maximum-subarray
#
# Given an integer array nums,
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
#
# Input: nums = [1]
# Output: 1
#
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
#
#
# Follow up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach,which is more subtle.
#

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_53.py")])
