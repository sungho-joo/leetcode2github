# @l2g 154 python3
# [154] Find Minimum in Rotated Sorted Array II
# Difficulty: Hard
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
#
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.For example,
# the array nums = [0,1,4,4,5,6,7] might become:
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
#
# Notice that rotating an array [a[0],a[1],a[2],...,a[n-1]] 1 time results in the array [a[n-1],a[0],
# a[1],a[2],...,a[n-2]].
# Given the sorted rotated array nums that may contain duplicates,
# return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
#
#
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates.Would this affect the runtime complexity? How and why?
#
#

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(mid):
            if nums[mid] < nums[-1]:
                return 1
            elif nums[mid] > nums[-1]:
                return -1
            else:
                if nums[0] != nums[-1]:
                    return 1
                else:
                    l, r = mid, mid
                    while l >= 0 and r < len(nums):
                        if nums[l] != nums[-1]:
                            return 1
                        if nums[r] != nums[-1]:
                            return -1
                        l -= 1
                        r += 1
                    if l < 0 and r > (len(nums) - 1):
                        return 0
                    elif l < 0:
                        return -1
                    else:
                        return 1

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            # print('mid', mid, 'condition', condition(mid))
            if condition(mid) == 1:
                r = mid
            elif condition(mid) == -1:
                l = mid + 1
            else:
                return nums[mid]

        return nums[l]


# basic idea
# comare elem with far right and far left

# 567
#    1234

# 1) if x < far right -> in second zone -> high = x
# 2) if x > far right -> in first zone -> low = x + 1
# 3) if x == far right -> can be in either first or second zone
#     -> check far left if it is same as far right
#         if x < far left: x in second zone
#         if x == far left -> can be in either zone
#         -> check either way using pointer to find sth different comes up


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_154.py")])
