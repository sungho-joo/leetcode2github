# @l2g 1839 python3
# [1839] Longest Substring Of All Vowels in Order
# Difficulty: Medium
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order
#
# A string is considered beautiful if it satisfies the following conditions:
#
# Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
# The letters must be sorted in alphabetical order (i.e.all 'a's before 'e's,all 'e's before 'i's,etc.
# ).
#
# For example,strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful,but "uaeio","aeoiu",
# and "aaaeeeooo" are not beautiful.
# Given a string word consisting of English vowels,
# return the length of the longest beautiful substring of word.If no such substring exists,return 0.
# A substring is a contiguous sequence of characters in a string.
#
# Example 1:
#
# Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
# Output: 13
# Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
# Example 2:
#
# Input: word = "aeeeiiiioooauuuaeiou"
# Output: 5
# Explanation: The longest beautiful substring in word is "aeiou" of length 5.
#
# Example 3:
#
# Input: word = "a"
# Output: 0
# Explanation: There is no beautiful substring, so return 0.
#
#
# Constraints:
#
# 1 <= word.length <= 5 * 10^5
# word consists of characters 'a', 'e', 'i', 'o', and 'u'.
#
#

from typing import Set


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        word += "a"  # for edge case of having u at the end of string
        alp_set: Set = set()
        ans = 0
        for ind, alp in enumerate(word):
            if alp_set:
                if alp < prev:
                    if len(alp_set) == 5:
                        ans = max(ans, ind - start_ind)
                    alp_set.clear()

            if not alp_set:
                start_ind = ind
            alp_set.add(alp)
            prev = alp
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1839.py")])
