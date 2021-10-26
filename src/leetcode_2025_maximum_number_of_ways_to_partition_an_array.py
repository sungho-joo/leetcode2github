# @l2g 2025 python3
# [2025] Maximum Number of Ways to Partition an Array
# Difficulty: Hard
# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array
#
# You are given a 0-indexed integer array nums of length n.
# The number of ways to partition nums is the number of pivot indices that satisfy both conditions:
#
# 1 <= pivot < n
# nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
#
# You are also given an integer k.You can choose to change the value of one element of nums to k,
# or to leave the array unchanged.
# Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.
#
# Example 1:
#
# Input: nums = [2,-1,2], k = 3
# Output: 1
# Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2].
# There is one way to partition the array:
# - For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
#
# Example 2:
#
# Input: nums = [0,0,0], k = 1
# Output: 2
# Explanation: The optimal approach is to leave the array unchanged.
# There are two ways to partition the array:
# - For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
# - For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
#
# Example 3:
#
# Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
# Output: 4
# Explanation: One optimal approach is to change nums[2] to k.The array becomes [22,4,-33,-20,-15,15,
# -16,7,19,-10,0,-13,-14].
# There are four ways to partition the array.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 10^5
# -10^5 <= k, nums[i] <= 10^5
#
#

import bisect
from typing import List


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)

        total_sum = sum(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]

        diff_dict = defaultdict(list)

        for i in range(1, n):
            front, back = presum[i], total_sum - presum[i]
            diff_dict[front - back].append(i - 1)

        num_of_syms = [0] * (n + 1)
        for i in range(n):
            change = k - nums[i]
            # Front
            f_index = bisect.bisect_left(diff_dict[-change], i)
            num_of_syms[i] += len(diff_dict[-change]) - f_index

            # Back
            b_index = bisect.bisect_left(diff_dict[change], i)
            num_of_syms[i] += b_index

        num_of_syms[-1] = len(diff_dict[0])
        return max(num_of_syms)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2025.py")])
