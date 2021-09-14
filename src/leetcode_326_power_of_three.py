# @l2g 326 python3
# [326] Power of Three
# Difficulty: Easy
# https://leetcode.com/problems/power-of-three
#
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
#
# Example 1:
# Input: n = 27
# Output: true
# Example 2:
# Input: n = 0
# Output: false
# Example 3:
# Input: n = 9
# Output: true
# Example 4:
# Input: n = 45
# Output: false
#
#
# Constraints:
#
# -2^31 <= n <= 2^31 - 1
#
#
# Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            div, rem = divmod(n, 3)
            if rem != 0:
                return False
            n = div
        return True if n == 1 else False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_326.py")])
