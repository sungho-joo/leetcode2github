# @l2g 5 python3
# [5] Longest Palindromic Substring
# Difficulty: Medium
# https://leetcode.com/problems/longest-palindromic-substring
#
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
# Example 3:
#
# Input: s = "a"
# Output: "a"
#
# Example 4:
#
# Input: s = "ac"
# Output: "a"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(i, j):
            if i < 0 or j > (len(s) - 1):
                return i + 1, j - 1
            if s[i] != s[j]:
                return i + 1, j - 1
            return is_palindrome(i - 1, j + 1)

        ans = ""
        for pos in range(len(s)):
            st, en = is_palindrome(pos, pos)
            ans = s[st : en + 1] if len(ans) < (en - st + 1) else ans
            if pos > 0 and s[pos] == s[pos - 1]:
                st, en = is_palindrome(pos - 1, pos)
                ans = s[st : en + 1] if len(ans) < (en - st + 1) else ans
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_5.py")])
