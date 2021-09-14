# @l2g 224 python3
# [224] Basic Calculator
# Difficulty: Hard
# https://leetcode.com/problems/basic-calculator
#
# Given a string s representing a valid expression,implement a basic calculator to evaluate it,
# and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
# such as eval().
#
# Example 1:
#
# Input: s = "1 + 1"
# Output: 2
#
# Example 2:
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation.
# '-' could be used as a unary operation but it has to be inside parentheses.
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.
#
#


class Solution:
    def calculate(self, s: str) -> int:
        def inside_parenthesis(pos):
            ans = 0
            prev_op = +1
            prev_num = ["0"]
            while pos < len(s):
                # Get full num
                if s[pos].isdecimal():
                    prev_num.append(s[pos])
                else:
                    # print(prev_num)
                    if prev_num:
                        ans += int("".join(prev_num)) * prev_op
                        prev_num = []
                if s[pos] == " ":
                    pass
                elif s[pos] == "-":
                    prev_op = -1
                elif s[pos] == "+":
                    prev_op = +1
                elif s[pos] == "(":
                    inside_num, end_pos = inside_parenthesis(pos + 1)
                    ans += prev_op * inside_num
                    pos = end_pos
                elif s[pos] == ")":
                    break
                pos += 1
            if prev_num:
                ans += int("".join(prev_num)) * prev_op
            return ans, pos

        ans, _ = inside_parenthesis(0)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_224.py")])
