# @l2g 1941 python3
# [1941] Check if All Characters Have Equal Number of Occurrences
# Difficulty: Easy
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences
#
# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e.,
# the same frequency).
#
# Example 1:
#
# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a','b',and 'c'.All characters occur 2 times in s.
#
# Example 2:
#
# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
#

from typing import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        return len(set(count.values())) == 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1941.py")])
