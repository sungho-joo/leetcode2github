# @l2g 40 python3
# [40] Combination Sum II
# Difficulty: Medium
# https://leetcode.com/problems/combination-sum-ii
#
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
# Constraints:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()

        def dfs(pos, path, remaining):
            if remaining == 0:
                ans.add(tuple(path))
                return

            duplicates = set()
            for next_pos in range(pos + 1, len(candidates)):
                if candidates[next_pos] <= remaining:
                    if candidates[next_pos] not in duplicates:
                        dfs(next_pos, path + [candidates[next_pos]], remaining - candidates[next_pos])
                        duplicates.add(candidates[next_pos])
                else:
                    break

        dfs(-1, [], target)
        return list(map(list, ans))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_40.py")])
