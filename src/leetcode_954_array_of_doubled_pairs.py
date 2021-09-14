# @l2g 954 python3
# [954] Array of Doubled Pairs
# Difficulty: Medium
# https://leetcode.com/problems/array-of-doubled-pairs
#
# Given an integer array of even length arr,
# return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2,
# or false otherwise.
#
# Example 1:
#
# Input: arr = [3,1,3,6]
# Output: false
#
# Example 2:
#
# Input: arr = [2,1,2,6]
# Output: false
#
# Example 3:
#
# Input: arr = [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
#
# Example 4:
#
# Input: arr = [1,2,4,16,8,4]
# Output: false
#
#
# Constraints:
#
# 2 <= arr.length <= 3 * 10^4
# arr.length is even.
# -10^5 <= arr[i] <= 10^5
#
#

from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        pos, neg = defaultdict(int), defaultdict(int)
        zeros = 0
        for num in arr:
            if num > 0:
                pos[num] += 1
            if num < 0:
                neg[num] += 1
            if num == 0:
                zeros += 1

        if zeros % 2 == 1:
            return False

        for k in sorted(pos):
            if pos[k] > pos[2 * k]:
                return False
            pos[2 * k] -= pos[k]

        for k in sorted(neg, reverse=True):
            if neg[k] > neg[2 * k]:
                return False
            neg[2 * k] -= neg[k]
        return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_954.py")])
