# @l2g 1911 python3
# [1911] Maximum Alternating Subsequence Sum
# Difficulty: Medium
# https://leetcode.com/problems/maximum-alternating-subsequence-sum
#
# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.
#
# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
#
# Given an array nums,
# return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).
#
#
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.
# For example,[2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements),while [2,4,
# 2] is not.
#
# Example 1:
#
# Input: nums = [4,2,5,3]
# Output: 7
# Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
#
# Example 2:
#
# Input: nums = [5,6,7,8]
# Output: 8
# Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
#
# Example 3:
#
# Input: nums = [6,2,1,2,4,5]
# Output: 10
# Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#


# @l2g 1911 python3
# [1911] Maximum Alternating Subsequence Sum
# Difficulty: Medium
# https://leetcode.com/problems/maximum-alternating-subsequence-sum
#
# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.
#
# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
#
# Given an array nums,
# return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).
#
#
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.
# For example,[2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements),while [2,4,
# 2] is not.
#
# Example 1:
#
# Input: nums = [4,2,5,3]
# Output: 7
# Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
#
# Example 2:
#
# Input: nums = [5,6,7,8]
# Output: 8
# Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
#
# Example 3:
#
# Input: nums = [6,2,1,2,4,5]
# Output: 10
# Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.append(-float("inf"))
        n = len(nums)
        if n == 1:
            return nums[0]

        incre = [] if nums[0] <= nums[1] else [(nums[0],)]
        cur_arr = []
        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                if len(cur_arr) == 0:
                    cur_arr.append(nums[i - 1])
                cur_arr.append(nums[i])
            else:
                if cur_arr:
                    incre.append(tuple(cur_arr))
                    cur_arr = []

        ans = []
        for i, v in enumerate(incre):
            if i == 0:
                ans.append(v[-1])
            else:
                ans.append(v[0])
                ans.append(v[-1])

        flip = 1
        ct = 0
        for num in ans:
            if flip:
                ct += num
            else:
                ct -= num

            flip ^= 1
        return ct


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1911.py")])
