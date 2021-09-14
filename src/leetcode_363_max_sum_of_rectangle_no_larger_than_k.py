# @l2g 363 python3
# [363] Max Sum of Rectangle No Larger Than K
# Difficulty: Hard
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k
#
# Given an m x n matrix matrix and an integer k,
# return the max sum of a rectangle in the matrix such that its sum is no larger than k.
# It is guaranteed that there will be a rectangle with a sum no larger than k.
#
# Example 1:
#
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0,1],[-2,3]] is 2,
# and 2 is the max number no larger than k (k = 2).
#
# Example 2:
#
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5
#
#
# Follow up: What if the number of rows is much larger than the number of columns?
#

import bisect
import math
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])

        def get_presum(arr):
            pre_sum = [0] * (m + 1)
            for i in range(m):
                pre_sum[i + 1] = pre_sum[i] + arr[i]
            return pre_sum

        def get_sum(arr, l, r):
            return arr[r + 1] - arr[l]

        def get_max_sum_1d(c1, c2):
            row_sums = [get_sum(self.pre_sum_mat[row], c1, c2) for row in range(n)]
            presums = [0, math.inf]
            cur_sum = 0
            ans = -math.inf
            for x in row_sums:
                cur_sum += x
                i = bisect.bisect_left(presums, cur_sum - k)
                ans = max(ans, cur_sum - presums[i])
                bisect.insort(presums, cur_sum)

            return ans

        # get pre_sum matrix n*m -> n*(m+1)
        self.pre_sum_mat = []
        for row in matrix:
            self.pre_sum_mat.append(get_presum(row))

        ans = -math.inf
        for c1 in range(m):
            for c2 in range(c1, m):
                ans = max(get_max_sum_1d(c1, c2), ans)
                if ans == k:
                    return ans

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_363.py")])
