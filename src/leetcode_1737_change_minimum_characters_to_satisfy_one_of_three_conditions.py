# @l2g 1737 python3
# [1737] Change Minimum Characters to Satisfy One of Three Conditions
# Difficulty: Medium
# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions
#
# You are given two strings a and b that consist of lowercase letters.In one operation,
# you can change any character in a or b to any lowercase letter.
# Your goal is to satisfy one of the following three conditions:
#
# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.
#
# Return the minimum number of operations needed to achieve your goal.
#
# Example 1:
#
# Input: a = "aba", b = "caa"
# Output: 2
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations,
# then every letter in b is less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).
#
# Example 2:
#
# Input: a = "dabadd", b = "cda"
# Output: 3
# Explanation: The best way is to make condition 1 true by changing b to "eee".
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 10^5
# a and b consist only of lowercase letters.
#
#

from typing import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        a_counter = Counter(ord(c) - 97 for c in a)
        b_counter = Counter(ord(c) - 97 for c in b)

        # Condition 3
        res = len_a + len_b - max((a_counter + b_counter).values())

        for i in range(25):
            a_counter[i + 1] += a_counter[i]
            b_counter[i + 1] += b_counter[i]

            res = min(res, len_a - a_counter[i] + b_counter[i])
            res = min(res, len_b - b_counter[i] + a_counter[i])

        return res


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1737.py")])
