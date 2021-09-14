# @l2g 1981 python3
# [1981] Minimize the Difference Between Target and Chosen Elements
# Difficulty: Medium
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements
#
# You are given an m x n integer matrix mat and an integer target.
# Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.
# Return the minimum absolute difference.
# The absolute difference between two numbers a and b is the absolute value of a - b.
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
# Output: 0
# Explanation: One possible choice is to:
# - Choose 1 from the first row.
# - Choose 5 from the second row.
# - Choose 7 from the third row.
# The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.
#
# Example 2:
#
#
# Input: mat = [[1],[2],[3]], target = 100
# Output: 94
# Explanation: The best possible choice is to:
# - Choose 1 from the first row.
# - Choose 2 from the second row.
# - Choose 3 from the third row.
# The sum of the chosen elements is 6, and the absolute difference is 94.
#
# Example 3:
#
#
# Input: mat = [[1,2,9,8,7]], target = 6
# Output: 1
# Explanation: The best choice is to choose 7 from the first row.
# The absolute difference is 1.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 70
# 1 <= mat[i][j] <= 70
# 1 <= target <= 800
#
#

import bisect
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        n, m = len(mat), len(mat[0])
        cur_sum = 0
        for row in mat:
            row.sort()
            cur_sum += row[0]

        if cur_sum > target:
            return cur_sum - target

        cur_sum_set = set([0])

        # upper_bound = target * 2
        for i, row in enumerate(mat):
            new_set = set()
            bigger_sum = None
            for cur_sum in iter(cur_sum_set):
                for col in row:
                    new_sum = cur_sum + col
                    if i == n - 1 and new_sum == target:
                        return 0
                    if new_sum > target:
                        if not bigger_sum:
                            bigger_sum = new_sum
                        if bigger_sum < new_sum:
                            break
                        elif bigger_sum > new_sum:
                            new_set.discard(bigger_sum)
                            bigger_sum = new_sum
                    new_set.add(cur_sum + col)
            cur_sum_set = new_set

        total_sums = sorted(list(cur_sum_set))
        first_candi = bisect.bisect_left(total_sums, target)
        if first_candi == len(total_sums):
            return abs(total_sums[-1] - target)
        elif first_candi == 0:
            return abs(total_sums[0] - target)
        else:
            second_candi = first_candi - 1
            return min(abs(total_sums[first_candi] - target), abs(total_sums[second_candi] - target))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1981.py")])
