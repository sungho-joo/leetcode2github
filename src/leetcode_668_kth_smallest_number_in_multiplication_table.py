# @l2g 668 python3
# [668] Kth Smallest Number in Multiplication Table
# Difficulty: Hard
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table
#
# Nearly everyone has used the Multiplication Table.
# The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
#
# Example 1:
#
#
# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.
#
# Example 2:
#
#
# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6th smallest number is 6.
#
#
# Constraints:
#
# 1 <= m, n <= 3 * 10^4
# 1 <= k <= m * n
#
#


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        matrix = list(range(1, n + 1))

        def condition(mid):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(mid // i, n)
            return cnt

        l, r = 1, m * n
        while l < r:
            mid = l + (r - l) // 2
            cnts = condition(mid)
            if cnts >= k:
                r = mid
            else:
                l = mid + 1

        return l


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_668.py")])
