# @l2g 415 python3
# [415] Add Strings
# Difficulty: Easy
# https://leetcode.com/problems/add-strings
#
# Given two non-negative integers,num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.
#
# Example 1:
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
# Example 2:
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
# Example 3:
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
#
#


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        num2 = "0" * (len(num1) - len(num2)) + num2
        circular_nums = {str(i): str(i + 1) for i in range(20)}

        add_dict = {}
        for i in range(10):
            for j in range(10):
                add_dict[(str(i), str(j))] = str(i + j)

        ans = []
        plus_one = False
        for i in range(len(num2)):
            ind = -1 - i
            next_num = add_dict[(num1[ind], num2[ind])]
            if plus_one:
                next_num = circular_nums[next_num]
            plus_one = True if len(next_num) == 2 else False
            ans.append(next_num[-1])

        if plus_one:
            ans.append("1")
        return "".join(ans)[::-1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_415.py")])
