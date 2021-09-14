# @l2g 300 python3
# [300] Longest Increasing Subsequence
# Difficulty: Medium
# https://leetcode.com/problems/longest-increasing-subsequence
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
# For example,[3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
#


# @l2g 300 python3
# [300] Longest Increasing Subsequence
# Difficulty: Medium
# https://leetcode.com/problems/longest-increasing-subsequence
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
# For example,[3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
#

import bisect
from typing import List


class Solution:
    # DP solution : bottom up
    # def lengthOfLIS(self, nums: List[int]) -> int:

    #     @lru_cache(None)
    #     def dp(pos):
    #         if pos == len(nums)-1:
    #             return 1

    #         ans = 0
    #         for next_pos in range(pos, len(nums)):
    #             if nums[pos] < nums[next_pos]:
    #                 ans = max(ans, dp(next_pos))
    #         return ans + 1

    #     ret = 0
    #     for i in range(len(nums)-1, -1, -1):
    #         ret = max(ret, dp(i))
    #     return ret

    # DP solution : top down
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     dp = [1] * n

    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #     return max(dp)

    # Binary search solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        sub = [nums[0]]
        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                ind = bisect.bisect_left(sub, nums[i])
                sub[ind] = nums[i]

        return len(sub)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_300.py")])
