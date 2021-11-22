# @l2g 2062 python3
# [2062] Count Vowel Substrings of a String
# Difficulty: Easy
# https://leetcode.com/problems/count-vowel-substrings-of-a-string
#
# A substring is a contiguous (non-empty) sequence of characters within a string.
# A vowel substring is a substring that only consists of vowels ('a','e','i','o',
# and 'u') and has all five vowels present in it.
# Given a string word, return the number of vowel substrings in word.
#
# Example 1:
#
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
#
# Example 2:
#
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
#
# Example 3:
#
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# Example 4:
#
# Input: word = "bbaeixoubb"
# Output: 0
# Explanation: The only substrings that contain all five vowels also contain consonants,
# so there are no vowel substrings.
#
#
# Constraints:
#
# 1 <= word.length <= 100
# word consists of lowercase English letters only.
#
#

from typing import Counter


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel_set = set(["a", "e", "i", "u", "o"])
        ans = 0
        count = Counter()
        for i, alp in enumerate(word):
            if alp in vowel_set:
                if i == 0 or word[i - 1] not in vowel_set:
                    left = pivot = i

                count[alp] += 1
                while len(count) == 5 and all(count.values()):
                    count[word[pivot]] -= 1
                    pivot += 1
                ans += pivot - left
            else:
                count = Counter()

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2062.py")])
