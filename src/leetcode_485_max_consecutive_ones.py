# @l2g 485 python3
# [485] Max Consecutive Ones
# Difficulty: Easy
# https://leetcode.com/problems/max-consecutive-ones
#
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
# Example 1:
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.
#
# Example 2:
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            if nums[i] != 1:
                cnt = 0
            ans = max(ans, cnt)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_485.py")])
