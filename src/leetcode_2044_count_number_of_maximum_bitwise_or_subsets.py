# @l2g 2044 python3
# [2044] Count Number of Maximum Bitwise-OR Subsets
# Difficulty: Medium
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets
#
# Given an integer array nums,
# find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
# Two subsets are considered different if the indices of the elements chosen are different.
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
#
# Example 1:
#
# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3.
# There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
#
# Example 2:
#
# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2.
# There are 2^3 - 1 = 7 total subsets.
#
# Example 3:
#
# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7.
# There are 6 subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
#
# Constraints:
#
# 1 <= nums.length <= 16
# 1 <= nums[i] <= 10^5
#
#

import functools
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # max_dim = int(math.log(max(nums)))
        max_num = functools.reduce(lambda x, y: x | y, nums)

        ans = 0
        for i in range(1, len(nums) + 1):
            for comb_num in combinations(nums, i):
                cal_num = reduce(lambda x, y: x | y, comb_num)
                if cal_num == max_num:
                    ans += 1
        return ans


#         dim_list = [[] for _ in range(max_dim+1)]
#         for num in nums:
#             for i in range(max_dim+1):
#                 if num & (1 << i): dim_list[i].append(num)

#         self.ans = 0
#         def dfs(pos, cur_num, visited):
#             if pos < 0:
#                 self.ans += 1
#                 return

#             if not dim_list[pos] or cur_num & (1 << pos):
#                 dfs(pos - 1, cur_num, visited)

#             for num in dim_list[pos]:
#                 if num not in visited:
#                     visited.add(num)
#                     dfs(pos-1, cur_num | num, visited)
#                     visited.discard(num)

#         dfs(max_dim, 0, set())
#         return self.ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2044.py")])
