# @l2g 2078 python3
# [2078] Two Furthest Houses With Different Colors
# Difficulty: Easy
# https://leetcode.com/problems/two-furthest-houses-with-different-colors
#
# There are n houses evenly lined up on the street,and each house is beautifully painted.
# You are given a 0-indexed integer array colors of length n,
# where colors[i] represents the color of the ith house.
# Return the maximum distance between two houses with different colors.
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
#
# Example 1:
#
#
# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer.
#
# Example 2:
#
#
# Input: colors = [1,8,3,8,3]
# Output: 4
# Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
# The furthest two houses with different colors are house 0 and house 4.
# House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
#
# Example 3:
#
# Input: colors = [0,1]
# Output: 1
# Explanation: The furthest two houses with different colors are house 0 and house 1.
# House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
#
#
# Constraints:
#
# n == colors.length
# 2 <= n <= 100
# 0 <= colors[i] <= 100
# Test data are generated such that at least two houses have different colors.
#
#

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        #         color_map = defaultdict(list)
        #         for i, color in enumerate(colors):
        #             if len(color_map[color]) <= 1:
        #                 color_map[color].append(i)
        #             else:
        #                 color_map[color][-1] = i
        n = len(colors)
        ans = -float("inf")
        # left
        for i in range(n):
            if colors[i] != colors[-1]:
                ans = max(ans, n - 1 - i)
                break

        # right
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                ans = max(ans, i)
                break
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2078.py")])
