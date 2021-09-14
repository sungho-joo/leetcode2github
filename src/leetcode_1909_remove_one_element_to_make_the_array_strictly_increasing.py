# @l2g 1909 python3
# [1909] Remove One Element to Make the Array Strictly Increasing
# Difficulty: Easy
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing
#
# Given a 0-indexed integer array nums,
# return true if it can be made strictly increasing after removing exactly one element,
# or false otherwise.If the array is already strictly increasing,return true.
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.
# length).
#
# Example 1:
#
# Input: nums = [1,2,10,5,7]
# Output: true
# Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
# [1,2,5,7] is strictly increasing, so return true.
#
# Example 2:
#
# Input: nums = [2,3,1,2]
# Output: false
# Explanation:
# [3,1,2] is the result of removing the element at index 0.
# [2,1,2] is the result of removing the element at index 1.
# [2,3,2] is the result of removing the element at index 2.
# [2,3,1] is the result of removing the element at index 3.
# No resulting array is strictly increasing, so return false.
# Example 3:
#
# Input: nums = [1,1,1]
# Output: false
# Explanation: The result of removing any element is [1,1].
# [1,1] is not strictly increasing, so return false.
#
# Example 4:
#
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is already strictly increasing, so return true.
#
#
# Constraints:
#
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
#
#


# @l2g 1909 python3
# [1909] Remove One Element to Make the Array Strictly Increasing
# Difficulty: Easy
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing
#
# Given a 0-indexed integer array nums,
# return true if it can be made strictly increasing after removing exactly one element,
# or false otherwise.If the array is already strictly increasing,return true.
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.
# length).
#
# Example 1:
#
# Input: nums = [1,2,10,5,7]
# Output: true
# Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
# [1,2,5,7] is strictly increasing, so return true.
#
# Example 2:
#
# Input: nums = [2,3,1,2]
# Output: false
# Explanation:
# [3,1,2] is the result of removing the element at index 0.
# [2,1,2] is the result of removing the element at index 1.
# [2,3,2] is the result of removing the element at index 2.
# [2,3,1] is the result of removing the element at index 3.
# No resulting array is strictly increasing, so return false.
# Example 3:
#
# Input: nums = [1,1,1]
# Output: false
# Explanation: The result of removing any element is [1,1].
# [1,1] is not strictly increasing, so return false.
#
# Example 4:
#
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is already strictly increasing, so return true.
#
#
# Constraints:
#
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
#
#

from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check_sorted(arr):
            # print(arr)
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True

        if check_sorted(nums):
            return True

        for i in range(len(nums)):
            if check_sorted(nums[:i] + nums[i + 1 :]):
                return True

        return False

        # reverse = []
        # for i in range(1, len(nums)):
        #     if nums[i] <= nums[i-1]:
        #         reverse.append(i)
        #     if len(reverse) > 1:
        #         return False

        # if len(reverse) == 0:
        #     return True
        # s, b = reverse[0] - 1, reverse[0]
        # if not check_sorted(nums[:s] + nums[s+1:]) and not check_sorted(nums[:b] + nums[b+1:]):
        #     return False
        # return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1909.py")])
