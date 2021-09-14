# @l2g 1662 python3
# [1662] Check If Two String Arrays are Equivalent
# Difficulty: Easy
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent
#
# Given two string arrays word1 and word2,return true if the two arrays represent the same string,
# and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
#
# Example 1:
#
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:
#
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
#
# Example 3:
#
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 10^3
# 1 <= word1[i].length, word2[i].length <= 10^3
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
# word1[i] and word2[i] consist of lowercase letters.
#
#

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        cur_str, compare_str = word1.pop(), word2.pop()
        while word1 or word2:
            len_compare_str = len(compare_str)
            if len(cur_str) < len_compare_str:
                cur_str = word1.pop() + cur_str
            else:
                if cur_str[-len_compare_str:] == compare_str:
                    cur_str = cur_str[:-len_compare_str]
                    compare_str = word2.pop()
                else:
                    return False

        if cur_str != compare_str:
            return False
        else:
            return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1662.py")])
