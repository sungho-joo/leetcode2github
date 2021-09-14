# @l2g 917 python3
# [917] Reverse Only Letters
# Difficulty: Easy
# https://leetcode.com/problems/reverse-only-letters
#
# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
#
# Return s after reversing it.
#
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
#
#


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            alpha_l = s[l].isalpha()
            alpha_r = s[r].isalpha()
            if alpha_l and alpha_r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif alpha_l and not alpha_r:
                r -= 1
            elif alpha_r and not alpha_l:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_917.py")])
