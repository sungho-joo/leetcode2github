# @l2g 371 python3
# [371] Sum of Two Integers
# Difficulty: Medium
# https://leetcode.com/problems/sum-of-two-integers
#
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
#
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
# -1000 <= a, b <= 1000
#
#


class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_num = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= max_num else ~(a ^ mask)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_371.py")])
