# @l2g 600 python3
# [600] Non-negative Integers without Consecutive Ones
# Difficulty: Hard
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones
#
# Given a positive integer n,return the number of the integers in the range [0,
# n] whose binary representations do not contain consecutive ones.
#
# Example 1:
#
# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them,only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
#
# Example 2:
#
# Input: n = 1
# Output: 2
#
# Example 3:
#
# Input: n = 2
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 10^9
#
#


class Solution:
    def findIntegers(self, n: int) -> int:
        b_n = bin(n + 1)[2:]
        dp = [1, 2] + [0] * (len(b_n) - 2)
        for i in range(2, len(b_n)):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        seen_one, ans = 0, 0
        for i in range(len(b_n)):
            if b_n[i] == "0":
                continue
            if seen_one == 1:
                break
            if i > 0 and b_n[i - 1] == "1":
                seen_one = True
            ans += dp[-i - 1]

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_600.py")])
