# @l2g 125 python3
# [125] Valid Palindrome
# Difficulty: Easy
# https://leetcode.com/problems/valid-palindrome
#
# Given a string s,determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Constraints:
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_valid = lambda alp: alp.isalpha() or alp.isdecimal()
        l, r = 0, len(s) - 1
        while l < r:
            if not is_valid(s[l]):
                l += 1
                continue
            if not is_valid(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_125.py")])
