# @l2g 1759 python3
# [1759] Count Number of Homogenous Substrings
# Difficulty: Medium
# https://leetcode.com/problems/count-number-of-homogenous-substrings
#
# Given a string s,return the number of homogenous substrings of s.Since the answer may be too large,
# return it modulo 10^9 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "abbcccaa"
# Output: 13
# Explanation: The homogenous substrings are listed as below:
# "a"   appears 3 times.
# "aa"  appears 1 time.
# "b"   appears 2 times.
# "bb"  appears 1 time.
# "c"   appears 3 times.
# "cc"  appears 2 times.
# "ccc" appears 1 time.
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
# Example 2:
#
# Input: s = "xy"
# Output: 2
# Explanation: The homogenous substrings are "x" and "y".
# Example 3:
#
# Input: s = "zzzzz"
# Output: 15
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of lowercase letters.
#


class Solution:
    def countHomogenous(self, s: str) -> int:
        # memory = defaultdict(int)
        prev = s[0]
        iter = 1
        ans = 1
        # memory[prev] += 1
        for value in s[1:]:
            if value == prev:
                iter += 1
                ans += iter
                # for ind in range(iter):
                # key = value * (ind + 1)
                # memory[key] += 1
            else:
                # memory[value] += 1
                prev = value
                ans += 1
                iter = 1
        # print(memory)
        # return sum(memory.values())
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1759.py")])
