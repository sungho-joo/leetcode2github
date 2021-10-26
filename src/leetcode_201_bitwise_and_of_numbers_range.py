# @l2g 201 python3
# [201] Bitwise AND of Numbers Range
# Difficulty: Medium
# https://leetcode.com/problems/bitwise-and-of-numbers-range
#
# Given two integers left and right that represent the range [left,right],
# return the bitwise AND of all numbers in this range,inclusive.
#
# Example 1:
#
# Input: left = 5, right = 7
# Output: 4
#
# Example 2:
#
# Input: left = 0, right = 0
# Output: 0
#
# Example 3:
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
# Constraints:
#
# 0 <= left <= right <= 2^31 - 1
#
#

import math


class Solution:
    def rangeBitwiseAnd(self, m, n):
        def get_dim(num):
            if num == 0:
                return 0
            return floor(math.log(num, 2))

        if get_dim(m) != get_dim(n):
            return 0

        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_201.py")])
