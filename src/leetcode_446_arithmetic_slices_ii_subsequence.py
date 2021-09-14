# @l2g 446 python3
# [446] Arithmetic Slices II - Subsequence
# Difficulty: Hard
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence
#
# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
#
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
#
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
#
# The test cases are generated so that the answer fits in 32-bit integer.
#
# Example 1:
#
# Input: nums = [2,4,6,8,10]
# Output: 7
# Explanation: All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#
# Example 2:
#
# Input: nums = [7,7,7,7,7]
# Output: 16
# Explanation: Any subsequence of this array is arithmetic.
#
#
# Constraints:
#
# 1  <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
#
#

import collections
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # dp state : position
        # dp value : number of arithmetic subsequences for each difference that ends with dp state
        # transition : move position forward(iterate all possible combi)
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                count = 0
                if diff in dp[j]:
                    count = dp[j][diff]
                dp[i][diff] += count + 1
                ans += count
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_446.py")])
