# @l2g 69 python3
# [69] Sqrt(x)
# Difficulty: Easy
# https://leetcode.com/problems/sqrtx
#
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer,the decimal digits are truncated,
# and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator,such as pow(x,0.
# 5) or x ** 0.5.
#
# Example 1:
#
# Input: x = 4
# Output: 2
#
# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842...,and since the decimal part is truncated,
# 2 is returned.
#
# Constraints:
#
# 0 <= x <= 2^31 - 1
#
#


class Solution:
    def mySqrt(self, x: int) -> int:
        next_num = x
        while next_num * next_num > x:
            next_num = (next_num + x / next_num) // 2
        return int(next_num)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_69.py")])