# @l2g 1840 python3
# [1840] Maximum Building Height
# Difficulty: Hard
# https://leetcode.com/problems/maximum-building-height
#
# You want to build n new buildings in a city.
# The new buildings will be built in a line and are labeled from 1 to n.
# However, there are city restrictions on the heights of the new buildings:
#
# The height of each building must be a non-negative integer.
# The height of the first building must be 0.
# The height difference between any two adjacent buildings cannot exceed 1.
#
# Additionally,there are city restrictions on the maximum height of specific buildings.
# These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi,
# maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.
# It is guaranteed that each building will appear at most once in restrictions,
# and building 1 will not be in restrictions.
# Return the maximum possible height of the tallest building.
#
# Example 1:
#
#
# Input: n = 5, restrictions = [[2,1],[4,1]]
# Output: 2
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.
# Example 2:
#
#
# Input: n = 6, restrictions = []
# Output: 5
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.
#
# Example 3:
#
#
# Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
# Output: 5
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3],
# and the tallest building has a height of 5.
#
#
# Constraints:
#
# 2 <= n <= 10^9
# 0 <= restrictions.length <= min(n - 1, 10^5)
# 2 <= idi <= n
# idi is unique.
# 0 <= maxHeighti <= 10^9
#
#

from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        # Keep in mind that building # 1 is always 0
        # Traverse rightward
        for i in range(len(restrictions) - 1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i + 1][1] = min(dist + restrictions[i][1], restrictions[i + 1][1])
        # Traverse leftward
        ans = 0
        for i in range(len(restrictions) - 1, 0, -1):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i - 1][1] = min(dist + restrictions[i][1], restrictions[i - 1][1])
            ans = max(
                ans,
                (
                    restrictions[i][1]
                    + restrictions[i - 1][1]
                    + restrictions[i][0]
                    - restrictions[i - 1][0]
                )
                // 2,
            )
        return max(ans, restrictions[-1][1] + n - restrictions[-1][0])


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1840.py")])
