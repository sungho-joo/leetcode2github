# @l2g 848 python3
# [848] Shifting Letters
# Difficulty: Medium
# https://leetcode.com/problems/shifting-letters
#
# You are given a string s of lowercase English letters and an integer array shifts of the same length.
# Call the shift() of a letter,the next letter in the alphabet,
# (wrapping around so that 'z' becomes 'a').
#
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
# Return the final string after all such shifts to s are applied.
#
# Example 1:
#
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
#
# Example 2:
#
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# shifts.length == s.length
# 0 <= shifts[i] <= 10^9
#
#

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        presum = [0] * (n + 1)
        for i in range(n, 0, -1):
            presum[i - 1] = (presum[i] + shifts[i - 1]) % 26

        get_shifted_alp = lambda alp, shift: chr(ord("a") + (ord(alp) - ord("a") + shift) % 26)

        ans = []
        for ind in range(len(shifts) - 1, -1, -1):
            ans.append(get_shifted_alp(s[ind], presum[ind]))

        return "".join(reversed(ans))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_848.py")])
