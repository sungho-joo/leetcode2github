# @l2g 633 python3
# [633] Sum of Square Numbers
# Difficulty: Medium
# https://leetcode.com/problems/sum-of-square-numbers
#
# Given a non-negative integer c,decide whether there're two integers a and b such that a^2 + b^2 = c.
#
# Example 1:
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
#
# Example 2:
#
# Input: c = 3
# Output: false
#
# Example 3:
#
# Input: c = 4
# Output: true
#
# Example 4:
#
# Input: c = 2
# Output: true
#
# Example 5:
#
# Input: c = 1
# Output: true
#
#
# Constraints:
#
# 0 <= c <= 2^31 - 1
#
#


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c)) + 1
        while l <= r:
            cal_num = l ** 2 + r ** 2
            if cal_num == c:
                return True
            if cal_num < c:
                l += 1
            if cal_num > c:
                r -= 1
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_633.py")])
