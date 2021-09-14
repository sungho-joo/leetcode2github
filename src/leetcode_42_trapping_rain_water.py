# @l2g 42 python3
# [42] Trapping Rain Water
# Difficulty: Hard
# https://leetcode.com/problems/trapping-rain-water
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,
# 1].In this case,6 units of rain water (blue section) are being trapped.
#
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # left to right
        left_sweep = [0] * n
        left_height = -1
        for i in range(n):
            if height[i] > left_height:
                left_height = height[i]

            left_sweep[i] = left_height
        # right to left
        right_sweep = [0] * n
        right_height = -1
        for i in range(n - 1, -1, -1):
            if height[i] > right_height:
                right_height = height[i]
            right_sweep[i] = right_height

        ans = 0
        for i in range(n):
            ans += min(right_sweep[i], left_sweep[i]) - height[i]

        return ans


if __name__ == "__main__":
    import pytest
    import os

    pytest.main([os.path.join("tests", "test_42.py")])
