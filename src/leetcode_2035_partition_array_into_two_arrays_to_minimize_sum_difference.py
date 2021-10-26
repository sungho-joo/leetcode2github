# @l2g 2035 python3
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
# Difficulty: Hard
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference
#
# You are given an integer array nums of 2 * n integers.
# You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays.
# To partition nums,put each element of nums into one of the two arrays.
# Return the minimum possible absolute difference.
#
# Example 1:
#
#
# Input: nums = [3,9,7,3]
# Output: 2
# Explanation: One optimal partition is: [3,9] and [7,3].
# The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
#
# Example 2:
#
# Input: nums = [-36,36]
# Output: 72
# Explanation: One optimal partition is: [-36] and [36].
# The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
#
# Example 3:
#
#
# Input: nums = [2,-1,0,4,-2,-9]
# Output: 0
# Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
# The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
#
#
# Constraints:
#
# 1 <= n <= 15
# nums.length == 2 * n
# -10^7 <= nums[i] <= 10^7
#
#

import bisect
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def get_sums(arr):
            m = len(arr)
            ans = [None] * (len(nums) // 2)

            for k in range(1, m):
                sums = []
                for comb in combinations(arr, k):
                    sums.append(sum(comb))
                ans[k] = sums
            return ans

        total_sum = sum(nums)
        n = len(nums)
        left_nums = nums[: n // 2]
        right_nums = nums[n // 2 :]

        left_sums = get_sums(left_nums)
        right_sums = get_sums(right_nums)

        ans = abs(sum(left_nums) - sum(right_nums))

        half = total_sum // 2

        for i in range(1, n // 2):
            left_sum_list = left_sums[i]
            right_sum_list = right_sums[n // 2 - i]
            right_sum_list.sort()

            for left_sum in left_sum_list:
                target = half - left_sum
                ind = bisect.bisect_left(right_sum_list, target)
                for right_index in [ind, ind - 1]:
                    if not 0 <= right_index < len(right_sum_list):
                        continue
                    half_sum = left_sum + right_sum_list[right_index]
                    ans = min(ans, abs(total_sum - 2 * half_sum))

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2035.py")])
