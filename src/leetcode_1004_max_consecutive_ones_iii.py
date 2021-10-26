# @l2g 1004 python3
# [1004] Max Consecutive Ones III
# Difficulty: Medium
# https://leetcode.com/problems/max-consecutive-ones-iii
#
# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
#
#

from typing import Counter, List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()
        ans = -float("inf")
        slow = 0
        for i in range(n):
            count[nums[i]] += 1
            if count[0] > k:
                count[nums[slow]] -= 1
                slow += 1
            ans = max(ans, i - slow + 1)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1004.py")])
