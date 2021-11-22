# @l2g 441 python3
# [441] Arranging Coins
# Difficulty: Easy
# https://leetcode.com/problems/arranging-coins
#
# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
#
# Example 2:
#
#
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
#
#
# Constraints:
#
# 1 <= n <= 2^31 - 1
#
#


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 2 ** 31

        while l < r:
            mid = l + (r - l) // 2
            if (mid * (mid + 1)) // 2 > n:
                r = mid
            else:
                l = mid + 1
        return l if ((l * (l + 1)) // 2) == n else l - 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_441.py")])
