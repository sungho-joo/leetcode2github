# @l2g 2048 python3
# [2048] Next Greater Numerically Balanced Number
# Difficulty: Medium
# https://leetcode.com/problems/next-greater-numerically-balanced-number
#
# An integer x is numerically balanced if for every digit d in the number x,
# there are exactly d occurrences of that digit in x.
# Given an integer n, return the smallest numerically balanced number strictly greater than n.
#
# Example 1:
#
# Input: n = 1
# Output: 22
# Explanation:
# 22 is numerically balanced since:
# - The digit 2 occurs 2 times.
# It is also the smallest numerically balanced number strictly greater than 1.
#
# Example 2:
#
# Input: n = 1000
# Output: 1333
# Explanation:
# 1333 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 1000.
# Note that 1022 cannot be the answer because 0 appeared more than 0 times.
#
# Example 3:
#
# Input: n = 3000
# Output: 3133
# Explanation:
# 3133 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 3000.
#
#
# Constraints:
#
# 0 <= n <= 10^6
#
#

import bisect
import itertools


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        candis = [[str(j) for _ in range(j)] for j in range(1, 7)]
        b_nums = set()

        for num_len in range(1, 7):
            for i in range(len(candis)):
                single_elem = int("".join(candis[i]))
                b_nums.add(single_elem)
                for j in range(i + 1, len(candis)):
                    if (len(candis[i]) + len(candis[j])) == num_len:
                        temp = candis[i] + candis[j]
                        perms = itertools.permutations(temp, len(temp))
                        perms = [int("".join(p)) for p in perms]
                        perms = set(perms)
                        b_nums |= perms

        temp = candis[0] + candis[1] + candis[2]
        perms = itertools.permutations(temp, len(temp))
        perms = [int("".join(p)) for p in perms]
        perms = set(perms)
        b_nums |= perms

        b_nums = sorted(b_nums)
        print(b_nums)
        ind = bisect.bisect_left(b_nums, n)
        if ind == len(b_nums):
            return 1224444
        if b_nums[ind] == n:
            if ind == (len(b_nums) - 1):
                return 1224444
            else:
                return b_nums[ind + 1]
        else:
            return b_nums[ind]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2048.py")])
