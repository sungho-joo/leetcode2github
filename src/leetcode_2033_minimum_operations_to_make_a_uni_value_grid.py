# @l2g 2033 python3
# [2033] Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid
#
# You are given a 2D integer grid of size m x n and an integer x.In one operation,
# you can add x to or subtract x from any element in the grid.
# A uni-value grid is a grid where all the elements of it are equal.
# Return the minimum number of operations to make the grid uni-value.If it is not possible,return -1.
#
# Example 1:
#
#
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following:
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.
#
# Example 2:
#
#
# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.
#
# Example 3:
#
#
# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# 1 <= x, grid[i][j] <= 10^4
#
#

from typing import Counter, List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total_nums = []
        for row in grid:
            total_nums.extend(row)

        total_nums.sort()
        count = Counter(total_nums)

        # every numb should have same remaining with x
        rem = total_nums[0] % x
        for key in count:
            if key % x != rem:
                return -1

        total_len = len(total_nums)
        a, b = divmod(total_len, 2)
        if b == 1:
            median_index = [a]
        else:
            median_index = [a, a - 1]

        ans = float("inf")
        for m_index in median_index:
            median_num = total_nums[m_index]
            temp_sum = 0
            for k, v in count.items():
                temp_sum += (abs(k - median_num) // x) * v
            ans = min(ans, temp_sum)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2033.py")])
