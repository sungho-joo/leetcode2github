# @l2g 658 python3
# [658] Find K Closest Elements
# Difficulty: Medium
# https://leetcode.com/problems/find-k-closest-elements
#
# Given a sorted integer array arr,two integers k and x,
# return the k closest integers to x in the array.The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
#
#

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k
        while low < high:
            mid = low + (high - low) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                high = mid
            else:
                low = mid + 1
        return arr[low : low + k]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_658.py")])
