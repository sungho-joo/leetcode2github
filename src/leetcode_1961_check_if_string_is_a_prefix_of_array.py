# @l2g 1961 python3
# [1961] Check If String Is a Prefix of Array
# Difficulty: Easy
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array
#
# Given a string s and an array of strings words, determine whether s is a prefix string of words.
# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.
# length.
# Return true if s is a prefix string of words, or false otherwise.
#
# Example 1:
#
# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# Explanation:
# s can be made by concatenating "i", "love", and "leetcode" together.
#
# Example 2:
#
# Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
# Output: false
# Explanation:
# It is impossible to make s using a prefix of arr.
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# 1 <= s.length <= 1000
# words[i] and s consist of only lowercase English letters.
#
#


# @l2g 1961 python3
# [1961] Check If String Is a Prefix of Array
# Difficulty: Easy
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array
#
# Given a string s and an array of strings words, determine whether s is a prefix string of words.
# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.
# length.
# Return true if s is a prefix string of words, or false otherwise.
#
# Example 1:
#
# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# Explanation:
# s can be made by concatenating "i", "love", and "leetcode" together.
#
# Example 2:
#
# Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
# Output: false
# Explanation:
# It is impossible to make s using a prefix of arr.
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# 1 <= s.length <= 1000
# words[i] and s consist of only lowercase English letters.
#
#

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        pos, word_idx = 0, 0
        while pos < len(s) and word_idx < len(words):
            if s[pos : pos + len(words[word_idx])] != words[word_idx]:
                return False
            pos += len(words[word_idx])
            word_idx += 1

        return True if pos == len(s) else False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1961.py")])
