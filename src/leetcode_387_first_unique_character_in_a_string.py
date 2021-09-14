# @l2g 387 python3
# [387] First Unique Character in a String
# Difficulty: Easy
# https://leetcode.com/problems/first-unique-character-in-a-string
#
# Given a string s,find the first non-repeating character in it and return its index.
# If it does not exist,return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        if all(v > 1 for v in count.values()):
            return -1
        for i, alp in enumerate(s):
            if count[alp] == 1:
                return i


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_387.py")])
