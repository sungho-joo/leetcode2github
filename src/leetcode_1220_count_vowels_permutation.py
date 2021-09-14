# @l2g 1220 python3
# [1220] Count Vowels Permutation
# Difficulty: Hard
# https://leetcode.com/problems/count-vowels-permutation
#
# Given an integer n,
# your task is to count how many strings of length n can be formed under the following rules:
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
#
# Example 2:
#
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae","ea","ei","ia","ie","io","iu","oi","ou" and "ua".
#
# Example 3:
#
# Input: n = 5
# Output: 68
#
# Constraints:
#
# 1 <= n <= 2 * 10^4
#
#


class Solution:
    MOD = 10 ** 9 + 7

    def countVowelPermutation(self, n: int) -> int:
        self.alp_map = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        res = 0
        for alp in self.alp_map:
            res += self.dp(alp, n)

        return res % self.MOD

    @lru_cache(None)
    def dp(self, alp, n):
        if n == 1:
            return 1
        ans = 0
        for next_alp in self.alp_map[alp]:
            ans += self.dp(next_alp, n - 1)
        return ans % self.MOD


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1220.py")])
