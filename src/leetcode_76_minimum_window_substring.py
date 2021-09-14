# @l2g 76 python3
# [76] Minimum Window Substring
# Difficulty: Hard
# https://leetcode.com/problems/minimum-window-substring
#
# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring,return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?

from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        target_num = len(t_count.keys())

        if not t_count.keys() <= s_count.keys():
            return ""

        l, r = 0, 0
        mutable = {k: 0 for k in s_count}
        missing = 0
        ans = ""

        while l < len(s):
            if missing < target_num:
                if r == len(s):
                    return ans
                mutable[s[r]] += 1
                if t_count[s[r]] > 0 and mutable[s[r]] == t_count[s[r]]:
                    missing += 1
                r += 1
            else:
                mutable[s[l]] -= 1
                if t_count[s[l]] > 0 and mutable[s[l]] == t_count[s[l]] - 1:
                    missing -= 1
                l += 1

            if missing == target_num:
                if not ans:
                    ans = s[l:r]
                elif (r - l) < len(ans):
                    ans = s[l:r]
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_76.py")])
