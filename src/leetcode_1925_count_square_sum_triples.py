# @l2g 1925 python3
# [1925] Count Square Sum Triples
# Difficulty: Easy
# https://leetcode.com/problems/count-square-sum-triples
#
# A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 + b^2 = c^2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
#
# Example 1:
#
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).
#
# Example 2:
#
# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
#
#
# Constraints:
#
# 1 <= n <= 250
#
#


class Solution:
    def countTriples(self, n: int) -> int:
        self.ans = 0
        sq_set = set([i ** 2 for i in range(1, n + 1)])

        def dp(num):
            if num > n:
                return 0

            for i in range(num + 1, n + 1):
                if num ** 2 + i ** 2 in sq_set:
                    self.ans += 1

            dp(num + 1)

        dp(1)
        return self.ans * 2


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1925.py")])
