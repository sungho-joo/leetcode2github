# @l2g 698 python3
# [698] Partition to K Equal Sum Subsets
# Difficulty: Medium
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets
#
# Given an integer array nums and an integer k,
# return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
#
# Example 1:
#
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
#
# Example 2:
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10^4
# The frequency of each element is in the range [1, 4].
#
#

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_num = sum(nums)
        a, b = divmod(total_num, k)
        if b != 0:
            return False
        nums.sort(reverse=True)

        ans = False

        @lru_cache(None)
        def dfs(mask, last):
            if mask == 0 and last == a:
                return True
            if last > a:
                return
            if last == a:
                last = 0

            for i in range(len(nums)):
                if mask & (1 << i):
                    if dfs(mask - (1 << i), last + nums[i]):
                        return True
            return False

        return dfs(2 ** len(nums) - 1, 0)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_698.py")])
