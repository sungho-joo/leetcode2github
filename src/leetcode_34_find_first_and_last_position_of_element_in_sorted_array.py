# @l2g 34 python3
# [34] Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
#
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
#

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def condition(arr, ind, _type):
            if _type == 1:
                return True if target <= arr[ind] else False
            else:
                return True if target < arr[ind] else False

        def binary_search(arr, target, _type):
            low, high = 0, len(nums) - 1
            while low < high:
                mid = low + (high - low) // 2
                if condition(arr, mid, _type):
                    high = mid
                else:
                    low = mid + 1
            return low

        ans_1 = binary_search(nums, target, 1)
        ans_2 = binary_search(nums, target, 2)
        if not nums or nums[ans_1] != target:
            return [-1, -1]

        return [ans_1, ans_2] if nums[ans_2] == target else [ans_1, ans_2 - 1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_34.py")])
