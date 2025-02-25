# @l2g 3 python3
# [3] Longest Substring Without Repeating Characters
# Difficulty: Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Example 4:
#
# Input: s = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = dict()
        start = 0
        for i, v in enumerate(s):
            if v in count:
                ans = max(ans, i - start)
                start = max(start, count[v] + 1)
            count[v] = i
        return max(ans, len(s) - start)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_3.py")])
