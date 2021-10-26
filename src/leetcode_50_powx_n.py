# @l2g 50 python3
# [50] Pow(x, n)
# Difficulty: Medium
# https://leetcode.com/problems/powx-n
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
# Example 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/2^2 = 1/4 = 0.25
#
#
# Constraints:
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= xn <= 10^4
#
#


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)
        if n % 2:
            return half * half * x
        else:
            return half * half


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_50.py")])
