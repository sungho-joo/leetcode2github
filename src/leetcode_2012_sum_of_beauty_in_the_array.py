# @l2g 2012 python3
# [2012] Sum of Beauty in the Array
# Difficulty: Medium
# https://leetcode.com/problems/sum-of-beauty-in-the-array
#
# You are given a 0-indexed integer array nums.For each index i (1 <= i <= nums.
# length - 2) the beauty of nums[i] equals:
#
# 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
# 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
# 0, if none of the previous conditions holds.
#
# Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation: For each index i in the range 1 <= i <= 1:
# - The beauty of nums[1] equals 2.
#
# Example 2:
#
# Input: nums = [2,4,6,4]
# Output: 1
# Explanation: For each index i in the range 1 <= i <= 2:
# - The beauty of nums[1] equals 1.
# - The beauty of nums[2] equals 0.
#
# Example 3:
#
# Input: nums = [3,2,1]
# Output: 0
# Explanation: For each index i in the range 1 <= i <= 1:
# - The beauty of nums[1] equals 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#

from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        biggest = [nums[0]] * n
        smallest = [nums[-1]] * n

        for i in range(1, n):
            biggest[i] = max(biggest[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            smallest[i] = min(smallest[i + 1], nums[i])

        # print(biggest, smallest)

        ans = 0
        for i in range(1, n - 1):
            if biggest[i - 1] < nums[i] < smallest[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2012.py")])
