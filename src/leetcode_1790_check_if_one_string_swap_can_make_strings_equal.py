# @l2g 1790 python3
# [1790] Check if One String Swap Can Make Strings Equal
# Difficulty: Easy
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal
#
# You are given two strings s1 and s2 of equal length.
# A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings.
# Otherwise,return false.
#
# Example 1:
#
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
#
# Example 2:
#
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
#
# Example 3:
#
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
#
# Example 4:
#
# Input: s1 = "abcd", s2 = "dcba"
# Output: false
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.
#
#


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff, diff_indices = 0, []
        for ind in range(len(s1)):
            if s1[ind] != s2[ind]:
                diff += 1
                diff_indices.append(ind)
            if diff > 2:
                return False
        if diff == 1:
            return False
        elif diff == 0:
            return True
        elif diff == 2:
            if (
                s1[diff_indices[0]] == s2[diff_indices[1]]
                and s1[diff_indices[1]] == s2[diff_indices[0]]
            ):
                return True
            else:
                return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1790.py")])
