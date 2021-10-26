# @l2g 215 python3
# [215] Kth Largest Element in an Array
# Difficulty: Medium
# https://leetcode.com/problems/kth-largest-element-in-an-array
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
#
#

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_215.py")])
