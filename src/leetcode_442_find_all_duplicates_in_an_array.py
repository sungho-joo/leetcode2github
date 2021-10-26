# @l2g 442 python3
# [442] Find All Duplicates in an Array
# Difficulty: Medium
# https://leetcode.com/problems/find-all-duplicates-in-an-array
#
# Given an integer array nums of length n where all the integers of nums are in the range [1,
# n] and each integer appears once or twice,return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
# Input: nums = [1]
# Output: []
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
#
#

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            cur_num = nums[i]
            if nums[abs(cur_num) - 1] < 0:
                ans.append(abs(cur_num))
            else:
                nums[abs(cur_num) - 1] *= -1
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_442.py")])
