# @l2g 378 python3
# [378] Kth Smallest Element in a Sorted Matrix
# Difficulty: Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
#
# Given an n x n matrix where each of the rows and columns are sorted in ascending order,
# return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15],
# and the 8th smallest number is 13
#
# Example 2:
#
# Input: matrix = [[-5]], k = 1
# Output: -5
#
#
# Constraints:
#
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n^2
#
#


# @l2g 378 python3
# [378] Kth Smallest Element in a Sorted Matrix
# Difficulty: Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
#
# Given an n x n matrix where each of the rows and columns are sorted in ascending order,
# return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15],
# and the 8th smallest number is 13
#
# Example 2:
#
# Input: matrix = [[-5]], k = 1
# Output: -5
#
#
# Constraints:
#
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n^2
#
#

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = [(row[0], 0, i) for i, row in enumerate(matrix)]
        heapq.heapify(min_heap)

        for _ in range(k):
            elem, col, row = heapq.heappop(min_heap)
            if col + 1 < len(matrix):
                heapq.heappush(min_heap, (matrix[row][col + 1], col + 1, row))
        return elem

        # low, high = matrix[0][0], matrix[-1][-1]

        # while low < high:
        #     mid = low + (high - low)//2
        #     if sum([bisect.bisect(row,mid) for row in matrix]) >= k:
        #         high = mid
        #     else:
        #         low = mid + 1
        # return low

        # n = len(matrix)
        # flat = []
        # for i in range(n):
        #     flat.extend(matrix[i])

        # flat.sort()
        # return flat[k-1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_378.py")])
