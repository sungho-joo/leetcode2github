# @l2g 16 python3
# [16] 3Sum Closest
# Difficulty: Medium
# https://leetcode.com/problems/3sum-closest
#
# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
#
# Input: nums = [0,0,0], target = 1
# Output: 0
#
#
# Constraints:
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        ans = float("inf")
        for i in range(n):
            num1 = nums[i]
            l, h = i + 1, n - 1
            while l < h:
                two_sum = nums[l] + nums[h]
                if two_sum < target - num1:
                    l += 1
                elif two_sum > target - num1:
                    h -= 1
                else:
                    return target
                three_sum = num1 + two_sum
                ans = ans if abs(ans - target) < abs(target - three_sum) else three_sum
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_16.py")])
