# @l2g 611 python3
# [611] Valid Triangle Number
# Difficulty: Medium
# https://leetcode.com/problems/valid-triangle-number
#
# Given an integer array nums,
# return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#
# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#


# @l2g 611 python3
# [611] Valid Triangle Number
# Difficulty: Medium
# https://leetcode.com/problems/valid-triangle-number
#
# Given an integer array nums,
# return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#
# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#

from typing import List


class Solution:
    # Using counter and binary search
    # def triangleNumber(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     sorted_dict = dict(sorted(count.items(), key=lambda x: x[0]))
    #     keys = list(sorted_dict.keys())

    #     presum = [0] * (len(keys) + 1)
    #     for i in range(len(keys)):
    #         presum[i+1] = presum[i] + sorted_dict[keys[i]]
    #     get_presum = lambda l, r: presum[r] - presum[l]

    #     ans = 0
    #     for s in range(len(sorted_dict)):
    #         if keys[s] == 0: continue
    #         ind = s
    #         for e in range(s, len(sorted_dict)):
    #             cur_sum = keys[s] + keys[e]
    #             ind = bisect.bisect_left(keys, cur_sum, ind)
    #             if s == e:
    #                 ans += math.comb(sorted_dict[keys[s]],3) if sorted_dict[keys[s]] > 2 else 0
    #                 cur_sum = math.comb(sorted_dict[keys[s]], 2) if sorted_dict[keys[s]] > 1 else 0
    #                 ans += cur_sum * get_presum(s+1, ind)
    #             elif s != e:
    #                 cur_sum = math.comb(sorted_dict[keys[e]], 2) if sorted_dict[keys[e]] > 1 else 0
    #                 ans += cur_sum * sorted_dict[keys[s]]
    #                 ans += sorted_dict[keys[s]] * sorted_dict[keys[e]] * get_presum(e+1, ind)
    #     return ans

    # Without counter
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums)):
            low, high = 0, i - 1

            while low < high:
                if nums[low] + nums[high] > nums[i]:
                    ans += high - low
                    high -= 1
                else:
                    low += 1
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_611.py")])
