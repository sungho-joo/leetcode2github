# @l2g 1711 python3
# [1711] Count Good Meals
# Difficulty: Medium
# https://leetcode.com/problems/count-good-meals
#
# A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
# You can pick any two different foods to make a good meal.
# Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food,
# return the number of different good meals you can make from this list modulo 10^9 + 7.
# Note that items with different indices are considered different even if they have the same deliciousness value.
#
# Example 1:
#
# Input: deliciousness = [1,3,5,7,9]
# Output: 4
# Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
# Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
#
# Example 2:
#
# Input: deliciousness = [1,1,1,3,3,3,7]
# Output: 15
# Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
#
# Constraints:
#
# 1 <= deliciousness.length <= 10^5
# 0 <= deliciousness[i] <= 2^20
#
#

from typing import Counter, List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counts = Counter()
        mod = 10 ** 9 + 7

        total = 0
        for x in deliciousness:
            for y in range(22):
                target = (1 << y) - x

                if target in counts:
                    total += counts[target]
            counts[x] += 1

        return total % mod


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1711.py")])
