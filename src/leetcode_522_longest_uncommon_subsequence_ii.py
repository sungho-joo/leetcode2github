# @l2g 522 python3
# [522] Longest Uncommon Subsequence II
# Difficulty: Medium
# https://leetcode.com/problems/longest-uncommon-subsequence-ii
#
# Given an array of strings strs,return the length of the longest uncommon subsequence between them.
# If the longest uncommon subsequence does not exist,return -1.
# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
#
# For example,
# "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc".
# Other subsequences of "aebdc" include "aebdc","aeb",and "" (empty string).
#
#
# Example 1:
# Input: strs = ["aba","cdc","eae"]
# Output: 3
# Example 2:
# Input: strs = ["aaa","aaa","aa"]
# Output: -1
#
#
# Constraints:
#
# 2 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] consists of lowercase English letters.
#
#

import collections
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check_subsequence(long_string, string):
            l_i, s_i = 0, 0
            while l_i < len(long_string) and s_i < len(string):
                if long_string[l_i] == string[s_i]:
                    l_i += 1
                    s_i += 1
                else:
                    l_i += 1

            return s_i == len(string)

        count = collections.Counter(strs)
        strs = sorted(strs, key=len, reverse=True)
        max_len = len(strs[0])
        max_strings = [k for k in count if len(k) == max_len]

        for i, string in enumerate(strs):
            # Longest string with count 1
            if count[string] == 1 and len(string) == max_len:
                return max_len

            # Shorter than longest string
            if len(string) < max_len and count[string] == 1:
                for l_string in max_strings:
                    if not check_subsequence(l_string, string):
                        return len(string)
        return -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_522.py")])
