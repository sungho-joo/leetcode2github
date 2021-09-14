# @l2g 7 python3
# [7] Reverse Integer
# Difficulty: Easy
# https://leetcode.com/problems/reverse-integer
#
# Given a signed 32-bit integer x,return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31,2^31 - 1],
# then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
#
#
# Constraints:
#
# -2^31 <= x <= 2^31 - 1
#
#


class Solution:
    def reverse(self, x: int) -> int:
        is_positive = True
        if x < 0:
            is_positive = False
            x *= -1

        upper_limit = 2 ** 31 - 1 if is_positive else 2 ** 31

        string_x = list(str(x))
        string_x.reverse()

        string_upper_limit = list(str(upper_limit))

        if len(string_x) >= len(string_upper_limit) and string_x > string_upper_limit:
            return 0

        ans = int("".join(string_x))
        return ans if is_positive else -ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_7.py")])
