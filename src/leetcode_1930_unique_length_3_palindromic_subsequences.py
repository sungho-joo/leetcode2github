# @l2g 1930 python3
# [1930] Unique Length-3 Palindromic Subsequences
# Difficulty: Medium
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences
#
# Given a string s,
# return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence,
# it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
#
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
#
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#


# @l2g 1930 python3
# [1930] Unique Length-3 Palindromic Subsequences
# Difficulty: Medium
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences
#
# Given a string s,
# return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence,
# it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
#
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
#
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#

import string


class Solution:
    # Presum version
    # def countPalindromicSubsequence(self, s: str) -> int:
    #     n = len(s)
    #     presum = [[0] * 26 for _ in range(n + 1)]
    #     for i in range(len(s)):
    #         presum[i + 1] = copy.copy(presum[i])
    #         presum[i + 1][ord(s[i]) - ord("a")] += 1

    #     alp_dict = defaultdict(list)
    #     for i in range(n):
    #         if s[i] in alp_dict:
    #             if len(alp_dict[s[i]]) == 1:
    #                 alp_dict[s[i]].append(i)
    #             else:
    #                 alp_dict[s[i]][1] = i
    #         else:
    #             alp_dict[s[i]].append(i)

    #     ans = 0
    #     for alp, num in alp_dict.items():
    #         if len(num) < 2:
    #             continue
    #         start, end = num
    #         for i in range(26):
    #             if presum[end][i] - presum[start + 1][i] > 0:
    #                 ans += 1

    #     return ans
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for alp in string.ascii_lowercase:
            i, j = s.find(alp), s.rfind(alp)
            if i != -1:
                ans += len(set(s[i + 1 : j]))
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1930.py")])
