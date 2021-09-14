# @l2g 28 python3
# [28] Implement strStr()
# Difficulty: Easy
# https://leetcode.com/problems/implement-strstr
#
# Implement strStr().
# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem,we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:
# Input: haystack = "", needle = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= haystack.length, needle.length <= 5 * 10^4
# haystack and needle consist of only lower-case English characters.
#
#


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # when needle is ""
        if not needle:
            return 0

        # when haystack is shorter than needle
        if len(haystack) < len(needle):
            return -1

        # find needle's index
        try:
            index = haystack.index(needle)
            return index
        except ValueError:
            return -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_28.py")])
