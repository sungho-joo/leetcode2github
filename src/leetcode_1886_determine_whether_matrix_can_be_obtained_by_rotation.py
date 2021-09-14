# @l2g 1886 python3
# [1886] Determine Whether Matrix Can Be Obtained By Rotation
# Difficulty: Easy
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
#
# Given two n x n binary matrices mat and target,
# return true if it is possible to make mat equal to target by rotating mat in 90-degree increments,
# or false otherwise.
#
# Example 1:
#
#
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
#
# Example 2:
#
#
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.
#
# Example 3:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
#
#
# Constraints:
#
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] and target[i][j] are either 0 or 1.
#
#

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for k in range(4):
            cur_target = [[0] * n for _ in range(n)]
            for i in range(n):
                cur_row = mat[i]
                for j in range(n):
                    cur_target[j][-1 - i] = cur_row[j]
            if cur_target == target:
                return True
            mat = list(cur_target)
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1886.py")])
