# @l2g 20 python3
# [20] Valid Parentheses
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses
#
# Given a string s containing just the characters '(',')','{','}','[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# Example 4:
#
# Input: s = "([)]"
# Output: false
#
# Example 5:
#
# Input: s = "{[]}"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {")": "(", "]": "[", "}": "{"}
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] in par_map and par_map[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return False if stack else True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_20.py")])
