# @l2g 915 python3
# [915] Partition Array into Disjoint Intervals
# Difficulty: Medium
# https://leetcode.com/problems/partition-array-into-disjoint-intervals
#
# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
#
# Return the length of left after such a partitioning.
# Test cases are generated such that partitioning exists.
#
# Example 1:
#
# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
#
# Example 2:
#
# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
# Constraints:
#
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# There is at least one valid answer for the given input.
#
#

import heapq
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        heap = [(nums[-1], len(nums) - 1)]
        biggest = nums[0]
        l, r = 0, len(nums)
        while l < r:
            # print(biggest, heap, l, r)
            if biggest <= heap[0][0]:
                heapq.heappush(heap, (nums[r - 1], r - 1))
                r -= 1
            else:
                max_ind = 0
                while biggest > heap[0][0]:
                    _, ind = heapq.heappop(heap)
                    max_ind = max(max_ind, ind)
                r = max_ind + 1
                biggest = max(biggest, max(nums[l : ind + 1]))
                l = ind

        return r + 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_915.py")])
