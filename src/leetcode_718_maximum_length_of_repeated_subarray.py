# @l2g 718 python3
# [718] Maximum Length of Repeated Subarray
# Difficulty: Medium
# https://leetcode.com/problems/maximum-length-of-repeated-subarray
#
# Given two integer arrays nums1 and nums2,
# return the maximum length of a subarray that appears in both arrays.
#
# Example 1:
#
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#
# Example 2:
#
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
#
#

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        short_list, long_list = (
            (nums2, nums1) if min(len(nums1), len(nums2)) == len(nums2) else (nums1, nums2)
        )
        n, m = len(short_list), len(long_list)
        dp, prev_dp = [0] * (n + 1), [0] * (n + 1)

        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if short_list[j - 1] == long_list[i - 1]:
                    dp[j] = prev_dp[j - 1] + 1
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])
            prev_dp, dp = dp, prev_dp

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_718.py")])
