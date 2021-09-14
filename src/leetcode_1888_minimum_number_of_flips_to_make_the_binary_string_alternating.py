# @l2g 1888 python3
# [1888] Minimum Number of Flips to Make the Binary String Alternating
# Difficulty: Medium
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating
#
# You are given a binary string s.
# You are allowed to perform two types of operations on the string in any sequence:
#
# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value,i.e.,
# if its value is '0' it becomes '1' and vice-versa.
#
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
# The string is called alternating if no two adjacent characters are equal.
#
# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
#
#
# Example 1:
#
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
#
# Example 2:
#
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
#
# Example 3:
#
# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
#
#


class Solution:
    def minFlips(self, s: str) -> int:
        a, b = divmod(len(s), 2)
        targets = ["10" * a + "1" * b, "01" * a + "0" * b]
        min_diff = 10 ** 5

        cumul_diff = [[0] * len(s) for _ in range(2)]
        total_diffs = []

        for i, target in enumerate(targets):
            diff = 0
            for j in range(len(s)):
                if target[j] != s[j]:
                    diff += 1
                    cumul_diff[i][j] = cumul_diff[i][j - 1] + 1 if j > 0 else 1
                else:
                    cumul_diff[i][j] = cumul_diff[i][j - 1] if j > 0 else 0
            min_diff = min(min_diff, diff)
            total_diffs.append(diff)
        # print(cumul_diff)

        if b == 0:
            return min_diff

        min_diff = 10 ** 5
        for i in range(len(s)):
            # start with 1, transform
            diff_1 = cumul_diff[0][i] + (total_diffs[1] - cumul_diff[1][i])
            diff_2 = cumul_diff[1][i] + (total_diffs[0] - cumul_diff[0][i])
            min_diff = min(min_diff, diff_1, diff_2)

        return min_diff


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1888.py")])
