# @l2g 2063 python3
# [2063] Vowels of All Substrings
# Difficulty: Medium
# https://leetcode.com/problems/vowels-of-all-substrings
#
# Given a string word,return the sum of the number of vowels ('a','e','i','o',
# and 'u') in every substring of word.
# A substring is a contiguous (non-empty) sequence of characters within a string.
# Note: Due to the large constraints,the answer may not fit in a signed 32-bit integer.
# Please be careful during the calculations.
#
# Example 1:
#
# Input: word = "aba"
# Output: 6
# Explanation:
# All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
# - "b" has 0 vowels in it
# - "a", "ab", "ba", and "a" have 1 vowel each
# - "aba" has 2 vowels in it
# Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6.
#
# Example 2:
#
# Input: word = "abc"
# Output: 3
# Explanation:
# All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
# - "a", "ab", and "abc" have 1 vowel each
# - "b", "bc", and "c" have 0 vowels each
# Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.
# Example 3:
#
# Input: word = "ltcd"
# Output: 0
# Explanation: There are no vowels in any substring of "ltcd".
# Example 4:
#
# Input: word = "noosabasboosa"
# Output: 237
# Explanation: There are a total of 237 vowels in all the substrings.
#
#
# Constraints:
#
# 1 <= word.length <= 10^5
# word consists of lowercase English letters.
#
#


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = defaultdict(list)
        for i, alp in enumerate(word):
            count[alp].append(i)

        vowels = ["a", "e", "i", "o", "u"]
        ans = 0
        for vowel in vowels:
            for cur_pos in count[vowel]:
                left, right = cur_pos + 1, n - cur_pos
                min_dist = min(left, right)
                max_dist = max(left, right)
                ans += ((min_dist) * (min_dist + 1)) // 2
                ans += min_dist * (max_dist - min_dist)
                rem = n - max_dist
                ans += ((rem) * (rem + 1)) // 2

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2063.py")])
