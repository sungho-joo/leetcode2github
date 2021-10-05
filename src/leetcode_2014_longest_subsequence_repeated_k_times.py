# @l2g 2014 python3
# [2014] Longest Subsequence Repeated k Times
# Difficulty: Hard
# https://leetcode.com/problems/longest-subsequence-repeated-k-times
#
# You are given a string s of length n,and an integer k.
# You are tasked to find the longest subsequence repeated k times in string s.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s,
# where seq * k represents a string constructed by concatenating seq k times.
#
# For example,"bba" is repeated 2 times in the string "bababcba",because the string "bbabba",
# constructed by concatenating "bba" 2 times,is a subsequence of the string "bababcba".
#
# Return the longest subsequence repeated k times in string s.If multiple such subsequences are found,
# return the lexicographically largest one.If there is no such subsequence,return an empty string.
#
# Example 1:
#
#
# Input: s = "letsleetcode", k = 2
# Output: "let"
# Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
# "let" is the lexicographically largest one.
#
# Example 2:
#
# Input: s = "bb", k = 2
# Output: "b"
# Explanation: The longest subsequence repeated 2 times is "b".
#
# Example 3:
#
# Input: s = "ab", k = 2
# Output: ""
# Explanation: There is no subsequence repeated 2 times. Empty string is returned.
#
# Example 4:
#
# Input: s = "bbabbabbbbabaababab", k = 3
# Output: "bbbb"
# Explanation: The longest subsequence "bbbb" is repeated 3 times in "bbabbabbbbabaababab".
#
#
# Constraints:
#
# n == s.length
# 2 <= n, k <= 2000
# 2 <= n < k * 8
# s consists of lowercase English letters.
#
#

from typing import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        count = Counter(s)
        max_pattern_len = n // k

        def check_existance(pat):
            new_pat = pat * k
            pat_ind, text_ind = 0, 0
            while pat_ind < len(new_pat) and text_ind < n:
                if new_pat[pat_ind] == s[text_ind]:
                    pat_ind += 1
                text_ind += 1
            return True if pat_ind == len(new_pat) else False

        candidates = [alp for alp, v in count.items() if v >= k]
        candidates.sort(reverse=True)
        if not candidates:
            return ""

        reversed_alps = candidates.copy()

        while candidates and len(candidates[0]) <= max_pattern_len:
            new_candis = []
            for pat in candidates:
                for alp in reversed_alps:
                    temp_pat = pat + alp
                    if check_existance(temp_pat):
                        new_candis.append(temp_pat)
            if not new_candis:
                return candidates[0]
            candidates = new_candis.copy()


"""
1. k와 n의 관계를 보면, n/k < 8이다. 즉, pattern의 길이는 최대 7
2. pattern은 lowercase english 이므로 26개이므로
즉, pattern의 complexity는 7개짜리 26 ** 7, 6개 짜리는 26 ** 6 ... 이다.
3. 이때 각 pattern의 반복 여부를 확인하는 건 O(n)으로 가능함.
4. additional time reduction은 presum으로 가능할듯.
"""


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2014.py")])
