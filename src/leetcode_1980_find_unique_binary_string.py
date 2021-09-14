# @l2g 1980 python3
# [1980] Find Unique Binary String
# Difficulty: Medium
# https://leetcode.com/problems/find-unique-binary-string
#
# Given an array of strings nums containing n unique binary strings each of length n,
# return a binary string of length n that does not appear in nums.If there are multiple answers,
# you may return any of them.
#
# Example 1:
#
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
#
# Example 2:
#
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
#
# Example 3:
#
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.
#
#

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set([int(num, 2) for num in nums])
        for i in range(len(nums) + 1):
            if i not in nums:
                ans = bin(i)[2:]
                if len(ans) < n:
                    return "0" * (n - len(ans)) + ans
                return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1980.py")])
