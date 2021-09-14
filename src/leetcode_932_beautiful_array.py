# @l2g 932 python3
# [932] Beautiful Array
# Difficulty: Medium
# https://leetcode.com/problems/beautiful-array
#
# An array nums of length n is beautiful if:
#
# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
#
# Given the integer n,return any beautiful array nums of length n.
# There will be at least one valid answer for the given n.
#
# Example 1:
# Input: n = 4
# Output: [2,1,4,3]
# Example 2:
# Input: n = 5
# Output: [3,1,2,5,4]
#
#
# Constraints:
#
# 1 <= n <= 1000
#
#

from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def split(arr):
            if len(arr) <= 2:
                return arr

            left, right = [], []
            for i in range(len(arr)):
                if i % 2:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            return split(left) + split(right)

        return split(list(range(1, n + 1)))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_932.py")])
