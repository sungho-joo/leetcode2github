# @l2g 1770 python3
# [1770] Maximum Score from Performing Multiplication Operations
# Difficulty: Medium
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations
#
# You are given two integer arrays nums and multipliers of size n and m respectively,where n >= m.
# The arrays are 1-indexed.
# You begin with a score of 0.You want to perform exactly m operations.
# On the ith operation (1-indexed),you will:
#
# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
#
# Return the maximum score after performing m operations.
#
# Example 1:
#
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# Example 2:
#
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
#
#
# Constraints:
#
# n == nums.length
# m == multipliers.length
# 1 <= m <= 10^3
# m <= n <= 10^5
# -1000 <= nums[i], multipliers[i] <= 1000
#
#

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.nums = nums
        self.multipliers = multipliers
        # self.memory: DefaultDict[List[int], int] = defaultdict(list)
        self.target_len = len(multipliers)
        self.num_len = len(nums)
        self.total_score = 0

        total_score = self.dfs(0, 0)
        # print(self.memory)
        return total_score

    # remember i th number added
    @lru_cache(2000)
    def dfs(self, left, i):
        # print(left, i)
        if i == self.target_len:
            return 0
        else:
            pickleft = self.dfs(left + 1, i + 1) + self.nums[left] * self.multipliers[i]
            pickright = (
                self.dfs(left, i + 1) + self.nums[self.num_len - 1 - (i - left)] * self.multipliers[i]
            )
        return max(pickleft, pickright)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1770.py")])
