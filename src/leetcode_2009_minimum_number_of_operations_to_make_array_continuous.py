# @l2g 2009 python3
# [2009] Minimum Number of Operations to Make Array Continuous
# Difficulty: Hard
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous
#
# You are given an integer array nums.In one operation,
# you can replace any element in nums with any integer.
# nums is considered continuous if both of the following conditions are fulfilled:
#
# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums equals nums.length - 1.
#
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.
# Return the minimum number of operations to make nums continuous.
#
# Example 1:
#
# Input: nums = [4,2,5,3]
# Output: 0
# Explanation: nums is already continuous.
#
# Example 2:
#
# Input: nums = [1,2,3,5,6]
# Output: 1
# Explanation: One possible solution is to change the last element to 4.
# The resulting array is [1,2,3,5,4], which is continuous.
#
# Example 3:
#
# Input: nums = [1,10,100,1000]
# Output: 3
# Explanation: One possible solution is to:
# - Change the second element to 2.
# - Change the third element to 3.
# - Change the fourth element to 4.
# The resulting array is [1,2,3,4], which is continuous.
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
#
#

import bisect
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_set = set(nums)
        sorted_key = sorted(num_set) + [float("inf")]
        max_occupied = -1
        for i in range(len(num_set)):
            range_end = sorted_key[i] + len(nums) - 1
            ind = bisect.bisect_left(sorted_key, range_end)
            if sorted_key[ind] == range_end:
                ind += 1
            max_occupied = max(max_occupied, ind - i)
            if ind == len(nums):
                break
        return len(nums) - max_occupied


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2009.py")])
