# @l2g 368 python3
# [368] Largest Divisible Subset
# Difficulty: Medium
# https://leetcode.com/problems/largest-divisible-subset
#
# Given a set of distinct positive integers nums,
# return the largest subset answer such that every pair (answer[i],
# answer[j]) of elements in this subset satisfies:
#
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
#
# If there are multiple solutions, return any of them.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
#
# Example 2:
#
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.
#
#

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        # dp state : pos
        # dp value : largest number of subset divisible by current position
        # dp transition : next smallest number dividing pos without remaining

        @lru_cache(None)
        def dp(pos):
            ans = [nums[pos]]
            for next_pos in range(pos + 1, len(nums)):
                if nums[next_pos] % nums[pos] == 0:
                    if len(dp(next_pos)) + 1 > len(ans):
                        ans = dp(next_pos) + [nums[pos]]
            return ans

        max_len = -float("inf")
        for i in range(len(nums)):
            if len(dp(i)) > max_len:
                ans = dp(i)
                max_len = len(dp(i))
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_368.py")])
