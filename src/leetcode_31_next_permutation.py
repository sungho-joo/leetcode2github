# @l2g 31 python3
# [31] Next Permutation
# Difficulty: Medium
# https://leetcode.com/problems/next-permutation
#
# Implement next permutation,
# which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible,it must rearrange it as the lowest possible order (i.e.,
# sorted in ascending order).
# The replacement must be in place and use only constant extra memory.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
# Input: nums = [1]
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:  # Get last descending position from the end
            i -= 1

        if i == 0:
            nums.reverse()
            return

        k = i - 1  # first ascending position from the end
        while nums[j] <= nums[k]:  # get smallest number that is bigger than nums[k]
            j -= 1

        nums[k], nums[j] = nums[j], nums[k]

        lo, hi = k + 1, len(nums) - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_31.py")])
