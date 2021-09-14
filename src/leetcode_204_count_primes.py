# @l2g 204 python3
# [204] Count Primes
# Difficulty: Easy
# https://leetcode.com/problems/count-primes
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example 1:
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# Example 2:
#
# Input: n = 0
# Output: 0
#
# Example 3:
#
# Input: n = 1
# Output: 0
#
#
# Constraints:
#
# 0 <= n <= 5 * 10^6
#
#


class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [i for i in range(n)]
        ans = 0
        for i in range(n):
            if i < 2:
                continue
            if nums[i] != -1:
                ans += 1
                for j in range(i * i, n, i):
                    nums[j] = -1

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_204.py")])
