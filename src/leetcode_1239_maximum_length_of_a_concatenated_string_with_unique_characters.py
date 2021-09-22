# @l2g 1239 python3
# [1239] Maximum Length of a Concatenated String with Unique Characters
# Difficulty: Medium
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
#
# Given an array of strings arr.
# String s is a concatenation of a sub-sequence of arr which have unique characters.
# Return the maximum possible length of s.
#
# Example 1:
#
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
#
# Example 2:
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
#
# Example 3:
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
#
#
# Constraints:
#
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.
#
#

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        set_chr = [set(alp) for alp in arr if len(alp) == len(set(alp))]

        ans = [0]

        def dfs(pos, cur_set):
            if ans[0] < len(cur_set):
                ans[0] = len(cur_set)

            for next_pos in range(pos, len(set_chr)):
                if not (set_chr[next_pos] & cur_set):
                    dfs(next_pos + 1, cur_set | set_chr[next_pos])

        dfs(0, set())
        return ans[0]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1239.py")])
