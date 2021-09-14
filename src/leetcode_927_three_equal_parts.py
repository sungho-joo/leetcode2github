# @l2g 927 python3
# [927] Three Equal Parts
# Difficulty: Hard
# https://leetcode.com/problems/three-equal-parts
#
# You are given an array arr which consists of only zeros and ones,
# divide the array into three non-empty parts such that all of these parts represent the same binary value.
# If it is possible, return any [i, j] with i + 1 < j, such that:
#
# arr[0], arr[1], ..., arr[i] is the first part,
# arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# All three parts have equal binary values.
#
# If it is not possible, return [-1, -1].
# Note that the entire part is used when considering what binary value it represents.For example,[1,1,
# 0] represents 6 in decimal,not 3.Also,leading zeros are allowed,so [0,1,1] and [1,
# 1] represent the same value.
#
# Example 1:
# Input: arr = [1,0,1,0,1]
# Output: [0,3]
# Example 2:
# Input: arr = [1,1,0,1,1]
# Output: [-1,-1]
# Example 3:
# Input: arr = [1,1,0,0,1]
# Output: [0,2]
#
#
# Constraints:
#
# 3 <= arr.length <= 3 * 10^4
# arr[i] is 0 or 1
#
#

import bisect
from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        presum_1 = [0] * n
        presum_1[0] = int(arr[0] == 1)
        for i in range(1, n):
            presum_1[i] = presum_1[i - 1] + int(arr[i] == 1)
        d, m = divmod(presum_1[-1], 3)
        if m != 0:
            return [-1, -1]
        if d == 0:
            return [0, 2]
        arr = list(map(str, arr))
        first_ind = bisect.bisect_left(presum_1, d)
        second_ind = bisect.bisect_left(presum_1, 2 * d, first_ind)

        target_num = int("".join(arr[second_ind + 1 :]), 2)
        first_num = int("".join(arr[: first_ind + 1]), 2)
        while first_num != target_num:
            first_ind += 1
            if arr[first_ind] == "1":
                return [-1, -1]
            first_num = first_num << 1

        # Found first_num
        second_num = int("".join(arr[first_ind + 1 : second_ind + 1]), 2)
        while second_num != target_num:
            second_ind += 1
            if arr[second_ind] == "1":
                return [-1, -1]
            second_num = second_num << 1

        return [first_ind, second_ind + 1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_927.py")])
