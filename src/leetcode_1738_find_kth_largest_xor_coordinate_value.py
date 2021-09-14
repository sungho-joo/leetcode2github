# @l2g 1738 python3
# [1738] Find Kth Largest XOR Coordinate Value
# Difficulty: Medium
# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value
#
# You are given a 2D matrix of size m x n,consisting of non-negative integers.
# You are also given an integer k.
# The value of coordinate (a,
# b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
# Find the kth largest value (1-indexed) of all the coordinates of matrix.
#
# Example 1:
#
# Input: matrix = [[5,2],[1,6]], k = 1
# Output: 7
# Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
# Example 2:
#
# Input: matrix = [[5,2],[1,6]], k = 2
# Output: 5
# Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
# Example 3:
#
# Input: matrix = [[5,2],[1,6]], k = 3
# Output: 4
# Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
# Example 4:
#
# Input: matrix = [[5,2],[1,6]], k = 4
# Output: 0
# Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0,
# which is the 4th largest value.
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 0 <= matrix[i][j] <= 10^6
# 1 <= k <= m * n
#
#

import heapq
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        heap: List = []

        temp = matrix[0][0]
        heapq.heappush(heap, -temp)
        for col in range(1, n):
            matrix[0][col] ^= temp
            heapq.heappush(heap, -matrix[0][col])
            temp = int(matrix[0][col])

        for row in range(1, m):
            for col in range(n):
                if col == 0:
                    temp_num = int(matrix[row][col])
                else:
                    temp_num ^= int(matrix[row][col])
                matrix[row][col] = matrix[row - 1][col] ^ temp_num
                heapq.heappush(heap, -matrix[row][col])

        for _ in range(k):
            ans = heapq.heappop(heap)

        print(matrix)

        return -ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1738.py")])
