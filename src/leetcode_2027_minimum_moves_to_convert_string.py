# @l2g 2027 python3
# [2027] Minimum Moves to Convert String
# Difficulty: Easy
# https://leetcode.com/problems/minimum-moves-to-convert-string
#
# You are given a string s consisting of n characters which are either 'X' or 'O'.
# A move is defined as selecting three consecutive characters of s and converting them to 'O'.
# Note that if a move is applied to the character 'O',it will stay the same.
# Return the minimum number of moves required so that all the characters of s are converted to 'O'.
#
# Example 1:
#
# Input: s = "XXX"
# Output: 1
# Explanation: XXX -> OOO
# We select all the 3 characters and convert them in one move.
#
# Example 2:
#
# Input: s = "XXOX"
# Output: 2
# Explanation: XXOX -> OOOX -> OOOO
# We select the first 3 characters in the first move, and convert them to 'O'.
# Then we select the last 3 characters and convert them so that the final string contains all 'O's.
# Example 3:
#
# Input: s = "OOOO"
# Output: 0
# Explanation: There are no 'X's in s to convert.
#
#
# Constraints:
#
# 3 <= s.length <= 1000
# s[i] is either 'X' or 'O'.
#
#


class Solution:
    def minimumMoves(self, s: str) -> int:
        split_s = list(s)
        ans = 0
        for i in range(len(s) - 2):
            if split_s[i] == "X":
                split_s[i : i + 3] = ["O"] * 3
                ans += 1

        if "X" in split_s[-2:]:
            ans += 1
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2027.py")])
