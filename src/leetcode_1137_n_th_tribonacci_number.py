# @l2g 1137 python3
# [1137] N-th Tribonacci Number
# Difficulty: Easy
# https://leetcode.com/problems/n-th-tribonacci-number
#
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
#
# Example 1:
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
# Example 2:
#
# Input: n = 25
# Output: 1389537
#
#
# Constraints:
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
#


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * 39
        dp[0], dp[1], dp[2] = 0, 1, 1
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1137.py")])
