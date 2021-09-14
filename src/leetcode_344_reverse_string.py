# @l2g 344 python3
# [344] Reverse String
# Difficulty: Easy
# https://leetcode.com/problems/reverse-string
#
# Write a function that reverses a string. The input string is given as an array of characters s.
#
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
#
#
# Follow up: Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
#

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse
        # s.reverse()
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_344.py")])
