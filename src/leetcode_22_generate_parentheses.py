# @l2g 22 python3
# [22] Generate Parentheses
# Difficulty: Medium
# https://leetcode.com/problems/generate-parentheses
#
# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses.
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8
#
#

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(arr, l, r):
            if l > r or l < 0 or r < 0:
                return
            if l == r == 0:
                ans.append("".join(arr))
                return

            dfs(arr + ["("], l - 1, r)
            dfs(arr + [")"], l, r - 1)

        dfs([], n, n)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_22.py")])
