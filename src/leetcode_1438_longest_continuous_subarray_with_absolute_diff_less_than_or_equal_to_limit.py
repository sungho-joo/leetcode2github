# @l2g 1438 python3
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Difficulty: Medium
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
#
# Given an array of integers nums and an integer limit,
# return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
#
# Example 1:
#
# Input: nums = [8,2,4,7], limit = 4
# Output: 2
# Explanation: All subarrays are:
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4.
# Therefore, the size of the longest subarray is 2.
#
# Example 2:
#
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4
# Explanation: The subarray [2,4,7,
# 2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
#
# Example 3:
#
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
#
#

import collections
from typing import List


class Solution:
    # 2 heap solution
    #     def longestSubarray(self, nums: List[int], limit: int) -> int:
    #         n = len(nums)

    #         l, r = 0, 0
    #         ans = -float('inf')
    #         min_heap, max_heap = [(nums[0], 0)], [(-nums[0], 0)]
    #         while r < n:
    #             if (-max_heap[0][0] - min_heap[0][0]) <= limit:
    #                 ans = max(ans, r - l + 1)
    #                 r += 1
    #                 if r == n: break
    #                 heapq.heappush(min_heap, (nums[r], r))
    #                 heapq.heappush(max_heap, (-nums[r], r))
    #             else:
    #                 l += 1
    #                 while min_heap[0][1] < l:
    #                     heapq.heappop(min_heap)

    #                 while max_heap[0][1] < l:
    #                     heapq.heappop(max_heap)

    #         return ans

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        minq = collections.deque()
        maxq = collections.deque()

        ans = -float("inf")
        i = 0
        for j in range(n):
            while minq and minq[-1] > nums[j]:
                minq.pop()
            while maxq and maxq[-1] < nums[j]:
                maxq.pop()

            minq.append(nums[j])
            maxq.append(nums[j])

            if maxq[0] - minq[0] > limit:
                if minq[0] == nums[i]:
                    minq.popleft()
                if maxq[0] == nums[i]:
                    maxq.popleft()
                i += 1
            ans = max(ans, j - i + 1)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1438.py")])
