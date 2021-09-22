# @l2g 978 python3
# [978] Longest Turbulent Subarray
# Difficulty: Medium
# https://leetcode.com/problems/longest-turbulent-subarray
#
# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
# More formally,a subarray [arr[i],arr[i + 1],...,
# arr[j]] of arr is said to be turbulent if and only if:
#
# For i <= k < j:
#
#
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
#
#
# Or, for i <= k < j:
#
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
#
#
#
#
# Example 1:
#
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
#
# Example 2:
#
# Input: arr = [4,8,12,16]
# Output: 2
#
# Example 3:
#
# Input: arr = [100]
# Output: 1
#
#
# Constraints:
#
# 1 <= arr.length <= 4 * 10^4
# 0 <= arr[i] <= 10^9
#
#

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        ans = 1 + int(arr[1] != arr[0])
        sub_len = ans
        prev = 2  # i-1 > i: 0, i-1 < i : 1, i-1 == i : 2
        for i in range(1, len(arr)):
            if prev == 0 and arr[i - 1] < arr[i]:
                sub_len += 1
            elif prev == 1 and arr[i - 1] > arr[i]:
                sub_len += 1
            else:
                ans = max(ans, sub_len)
                sub_len = 1 + int(arr[i - 1] != arr[i])
            if arr[i - 1] < arr[i]:
                prev = 1
            if arr[i - 1] > arr[i]:
                prev = 0
            if arr[i - 1] == arr[i]:
                prev = 2
        return max(ans, sub_len)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_978.py")])
