# @l2g 77 python3
# [77] Combinations
# Difficulty: Medium
# https://leetcode.com/problems/combinations
#
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.
#
# Example 1:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n
#
#

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(pos, stack):
            if len(stack) == k:
                ans.append(stack)
                return

            for next_num in range(pos + 1, n + 1):
                dfs(next_num, stack + [next_num])
            return

        for i in range(1, n - k + 2):
            dfs(i, [i])

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_77.py")])
