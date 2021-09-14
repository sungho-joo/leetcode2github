# @l2g 1819 python3
# [1819] Number of Different Subsequences GCDs
# Difficulty: Hard
# https://leetcode.com/problems/number-of-different-subsequences-gcds
#
# You are given an array nums that consists of positive integers.
# The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.
#
# For example, the GCD of the sequence [4,6,16] is 2.
#
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
#
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
#
# Return the number of different GCDs among all non-empty subsequences of nums.
#
# Example 1:
#
#
# Input: nums = [6,10,3]
# Output: 5
# Explanation: The figure shows all the non-empty subsequences and their GCDs.
# The different GCDs are 6, 10, 3, 2, and 1.
#
# Example 2:
#
# Input: nums = [5,15,40,5,6]
# Output: 7
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 2 * 10^5
#
#

import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        num_set = list(set(nums))
        biggest = max(num_set) + 1
        seen = [0] * biggest
        for num in num_set:
            seen[num] = 1

        ans = 0

        for j in range(1, biggest):
            running_gcd = 0
            # Check if j is gcd
            for num in range(j, biggest, j):
                if seen[num]:
                    running_gcd = math.gcd(running_gcd, num)
                    if running_gcd == j:
                        break
            ans += running_gcd == j

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1819.py")])
