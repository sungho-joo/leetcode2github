# @l2g 172 python3
# [172] Factorial Trailing Zeroes
# Difficulty: Medium
# https://leetcode.com/problems/factorial-trailing-zeroes
#
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
#
# Example 1:
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Example 3:
#
# Input: n = 0
# Output: 0
#
#
# Constraints:
#
# 0 <= n <= 10^4
#
#
# Follow up: Could you write a solution that works in logarithmic time complexity?
#


class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_5 = 0
        num = 5
        while num <= n:
            cnt_5 += n // num
            num *= 5
        return cnt_5


#         cnt_2 = 0
#         num = 2
#         while num <= n:
#             cnt_2 += n // num
#             num *= 2

#         return min(cnt_2, cnt_5)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_172.py")])
