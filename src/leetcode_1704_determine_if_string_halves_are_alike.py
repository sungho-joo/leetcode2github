# @l2g 1704 python3
# [1704] Determine if String Halves Are Alike
# Difficulty: Easy
# https://leetcode.com/problems/determine-if-string-halves-are-alike
#
# You are given a string s of even length.Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a','e','i','o','u','A','E','I','O',
# 'U').Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
#
# Example 1:
#
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
#
# Example 2:
#
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book".a has 1 vowel whereas b has 2.Therefore,they are not alike.
# Notice that the vowel o is counted twice.
#
# Example 3:
#
# Input: s = "MerryChristmas"
# Output: false
#
# Example 4:
#
# Input: s = "AbCdEfGh"
# Output: true
#
#
# Constraints:
#
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
#
#


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u"]
        s = s.lower()
        str_len = len(s) // 2
        first_half = s[:str_len]
        second_half = s[str_len:]
        count1, count2 = 0, 0
        for i in range(str_len):
            if first_half[i] in vowels:
                count1 += 1
            if second_half[i] in vowels:
                count2 += 1
        if count1 == count2:
            return True
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1704.py")])
