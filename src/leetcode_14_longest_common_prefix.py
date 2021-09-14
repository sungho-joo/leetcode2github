# @l2g 14 python3
# [14] Longest Common Prefix
# Difficulty: Easy
# https://leetcode.com/problems/longest-common-prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
#
#

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check_strings(alp, pos):
            for string in strs:
                if alp != string[pos]:
                    return False
            return True

        ans = [""]
        for i, alp in enumerate(min(strs, key=len)):
            if check_strings(alp, i):
                ans.append(alp)
            else:
                break
        return "".join(ans)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_14.py")])
