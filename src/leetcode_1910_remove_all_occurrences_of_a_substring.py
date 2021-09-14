# @l2g 1910 python3
# [1910] Remove All Occurrences of a Substring
# Difficulty: Medium
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring
#
# Given two strings s and part,
# perform the following operation on s until all occurrences of the substring part are removed:
#
# Find the leftmost occurrence of the substring part and remove it from s.
#
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.
#
# Example 1:
#
# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".
#
# Example 2:
#
# Input: s = "axxxxyyyyb", part = "xy"
# Output: "ab"
# Explanation: The following operations are done:
# - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
# - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
# - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
# - s = "axyb", remove "xy" starting at index 1 so s = "ab".
# Now s has no occurrences of "xy".
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s​​​​​​ and part consists of lowercase English letters.
#
#


# @l2g 1910 python3
# [1910] Remove All Occurrences of a Substring
# Difficulty: Medium
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring
#
# Given two strings s and part,
# perform the following operation on s until all occurrences of the substring part are removed:
#
# Find the leftmost occurrence of the substring part and remove it from s.
#
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.
#
# Example 1:
#
# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".
#
# Example 2:
#
# Input: s = "axxxxyyyyb", part = "xy"
# Output: "ab"
# Explanation: The following operations are done:
# - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
# - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
# - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
# - s = "axyb", remove "xy" starting at index 1 so s = "ab".
# Now s has no occurrences of "xy".
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s​​​​​​ and part consists of lowercase English letters.
#
#


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        len_p = len(part)

        def find_part(arr, prev):
            start = prev - len_p if prev > len_p else 0
            return arr.find(part, start)

        prev = 0
        ct = 0
        while prev > -1:
            prev = find_part(s, prev - 1)
            if prev == -1:
                break
            s = s[:prev] + s[prev + len_p :]
        return s


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1910.py")])
