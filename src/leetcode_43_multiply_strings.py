# @l2g 43 python3
# [43] Multiply Strings
# Difficulty: Medium
# https://leetcode.com/problems/multiply-strings
#
# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2,also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
#
#


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = []

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                f_num = (ord(n1) - ord("0")) * (10 ** i)
                s_num = (ord(n2) - ord("0")) * (10 ** j)
                ans.append(f_num * s_num)

        return str(sum(ans))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_43.py")])
