# @l2g 347 python3
# [347] Top K Frequent Elements
# Difficulty: Medium
# https://leetcode.com/problems/top-k-frequent-elements
#
# Given an integer array nums and an integer k,return the k most frequent elements.
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#

from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = defaultdict(list)
        for key, value in count.items():
            bucket[value].append(key)
        ans = []
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                ans.extend(bucket[i])
                k -= len(bucket[i])
            if k == 0:
                break
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_347.py")])
