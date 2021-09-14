# @l2g 47 python3
# [47] Permutations II
# Difficulty: Medium
# https://leetcode.com/problems/permutations-ii
#
# Given a collection of numbers,nums,that might contain duplicates,
# return all possible unique permutations in any order.
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
# Example 2:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(path, remaining):
            if not remaining:
                ans.append(path)

            added_nums = set()
            for i in range(len(remaining)):
                if remaining[i] not in added_nums:
                    dfs(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])
                    added_nums.add(remaining[i])

        dfs([], nums)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_47.py")])
