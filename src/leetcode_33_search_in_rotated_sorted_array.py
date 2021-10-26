# @l2g 33 python3
# [33] Search in Rotated Sorted Array
# Difficulty: Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function,
# nums is possibly rotated at an unknown pivot index k (1 <= k < nums.
# length) such that the resulting array is [nums[k],nums[k+1],...,nums[n-1],nums[0],nums[1],...,
# nums[k-1]] (0-indexed).For example,[0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,
# 5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums,or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
#
#

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(nums, mid, target):
            # Normal case
            if nums[0] < nums[-1]:
                return False if nums[mid] < target else True
            if target <= nums[-1]:
                if nums[0] <= nums[mid]:
                    return False
                return False if nums[mid] <= target else True
            else:
                if nums[mid] <= nums[-1]:
                    return True
                return False if nums[mid] <= target else True

        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if condition(nums, mid, target):
                high = mid
            else:
                low = mid + 1
        return low if nums[low] == target else -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_33.py")])
