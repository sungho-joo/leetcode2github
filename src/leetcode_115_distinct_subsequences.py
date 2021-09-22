# @l2g 115 python3
# [115] Distinct Subsequences
# Difficulty: Hard
# https://leetcode.com/problems/distinct-subsequences
#
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions.
# (i.e.,"ACE" is a subsequence of "ABCDE" while "AEC" is not).
# It is guaranteed the answer fits on a 32-bit signed integer.
#
# Example 1:
#
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# rabbbit
# rabbbit
# rabbbit
#
# Example 2:
#
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
# Constraints:
#
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.
#
#


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(s_pos, t_pos):
            if t_pos == len(t):
                return 1
            if s_pos == len(s):
                return 0

            ans = dfs(s_pos + 1, t_pos)
            return ans if s[s_pos] != t[t_pos] else ans + dfs(s_pos + 1, t_pos + 1)

        return dfs(0, 0)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_115.py")])
