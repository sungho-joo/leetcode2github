# @l2g 424 python3
# [424] Longest Repeating Character Replacement
# Difficulty: Medium
# https://leetcode.com/problems/longest-repeating-character-replacement
#
# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
#
#

from typing import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = Counter()
        ans = -float("inf")
        slow, max_f = 0, 0
        for i in range(n):
            count[s[i]] += 1
            max_f = max(max_f, count[s[i]])
            if i - slow + 1 - max_f > k:
                count[s[slow]] -= 1
                slow += 1
            ans = max(ans, i - slow + 1)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_424.py")])
