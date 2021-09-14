# @l2g 2002 python3
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
# Difficulty: Medium
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences
#
# Given a string s,
# find two disjoint palindromic subsequences of s such that the product of their lengths is maximized.
# The two subsequences are disjoint if they do not both pick a character at the same index.
# Return the maximum possible product of the lengths of the two palindromic subsequences.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# A string is palindromic if it reads the same forward and backward.
#
# Example 1:
#
#
# Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
# The product of their lengths is: 3 * 3 = 9.
#
# Example 2:
#
# Input: s = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
# The product of their lengths is: 1 * 1 = 1.
#
# Example 3:
#
# Input: s = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
# The product of their lengths is: 5 * 5 = 25.
#
#
# Constraints:
#
# 2 <= s.length <= 12
# s consists of lowercase English letters only.
#
#


class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(arr):
            if not arr:
                return True
            if arr[len(arr) - 1] != arr[0]:
                return False
            return is_palindrome(arr[1 : len(arr) - 1])

        ans = []

        def dfs(mask, pos, arr):
            if is_palindrome(arr) and len(arr) != 0:
                ans.append((mask, len(arr)))

            if pos == len(s):
                return

            for i in range(pos, len(s)):
                if not mask & (1 << i):
                    dfs(mask + (1 << i), i + 1, arr + [s[i]])

        dfs(0, 0, [])

        ret = -float("inf")
        ans_len = len(ans)
        for i in range(ans_len):
            for j in range(i + 1, ans_len):
                if ans[i][0] & ans[j][0] == 0:
                    ret = max(ret, ans[i][1] * ans[j][1])
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2002.py")])
