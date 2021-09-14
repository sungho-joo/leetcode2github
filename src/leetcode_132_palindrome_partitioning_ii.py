# @l2g 132 python3
# [132] Palindrome Partitioning II
# Difficulty: Hard
# https://leetcode.com/problems/palindrome-partitioning-ii
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example 1:
#
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
# Example 2:
#
# Input: s = "a"
# Output: 0
#
# Example 3:
#
# Input: s = "ab"
# Output: 1
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.
#
#


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def is_palindrome(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False

            return is_palindrome(l + 1, r - 1)

        @lru_cache(None)
        def dp(i):  # dp(i) : i ~ n 까지에서 palindrome의 최소 개수(즉, 최소 cut)
            if i == n:
                return 0

            ans = float("inf")
            for j in range(i, n):
                if is_palindrome(i, j):
                    ans = min(ans, dp(j + 1) + 1)
            return ans

        return dp(0) - 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_132.py")])
