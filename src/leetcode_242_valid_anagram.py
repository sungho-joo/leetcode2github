# @l2g 242 python3
# [242] Valid Anagram
# Difficulty: Easy
# https://leetcode.com/problems/valid-anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
#

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        return s_count == t_count


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_242.py")])