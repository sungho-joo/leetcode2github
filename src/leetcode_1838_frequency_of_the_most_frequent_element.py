# @l2g 1838 python3
# [1838] Frequency of the Most Frequent Element
# Difficulty: Medium
# https://leetcode.com/problems/frequency-of-the-most-frequent-element
#
# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k.In one operation,
# you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.
#
# Example 1:
#
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,
# 4,4].
# 4 has a frequency of 3.
# Example 2:
#
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
#
# Example 3:
#
# Input: nums = [3,9,6], k = 2
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
#
#

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums = nums + [10 ** 6]
        a, b = 0, 0
        sum = 0
        ans = 0
        while b < len(nums) - 1:
            # print(a, b, sum)
            if sum + (b - a + 1) * (nums[b + 1] - nums[b]) <= k:
                sum += (b - a + 1) * (nums[b + 1] - nums[b])
                b += 1
            else:
                sum -= nums[b] - nums[a]
                a += 1
            # print(a,b,sum)
            ans = max(ans, b - a)
        # print(ans)
        return max(ans + 1, 1)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1838.py")])
