# @l2g 540 python3
# [540] Single Element in a Sorted Array
# Difficulty: Medium
# https://leetcode.com/problems/single-element-in-a-sorted-array
#
# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search
        # if single number is before current position, even number index would have have different next element
        def condition(mid):
            if mid % 2 == 0:
                return nums[mid] != nums[mid + 1]
            else:
                return nums[mid] == nums[mid + 1]

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return nums[l]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_540.py")])
