# @l2g 17 python3
# [17] Letter Combinations of a Phone Number
# Difficulty: Medium
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
#
# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
#
# Input: digits = ""
# Output: []
#
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []

        def dfs(pos, arr):
            if pos == len(digits):
                if arr:
                    ans.append("".join(arr))
                return

            for alp in digit_map[digits[pos]]:
                dfs(pos + 1, arr + [alp])

        dfs(0, [])
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_17.py")])
