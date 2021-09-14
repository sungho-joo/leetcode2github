# @l2g 1674 python3
# [1674] Minimum Moves to Make Array Complementary
# Difficulty: Medium
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary
#
# You are given an integer array nums of even length n and an integer limit.In one move,
# you can replace any integer from nums with another integer between 1 and limit,inclusive.
# The array nums is complementary if for all indices i (0-indexed),
# nums[i] + nums[n - 1 - i] equals the same number.For example,the array [1,2,3,
# 4] is complementary because for all indices i,nums[i] + nums[n - 1 - i] = 5.
# Return the minimum number of moves required to make nums complementary.
#
# Example 1:
#
# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
#
# Example 2:
#
# Input: nums = [1,2,2,1], limit = 2
# Output: 2
# Explanation: In 2 moves,you can change nums to [2,2,2,2].
# You cannot change any number to 3 since 3 > limit.
#
# Example 3:
#
# Input: nums = [1,2,1,2], limit = 2
# Output: 0
# Explanation: nums is already complementary.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 10^5
# 1 <= nums[i] <= limit <= 10^5
# n is even.
#
#

from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        def get_range(pair):
            sum_of_num = sum(pair)
            smaller_num = min(pair)
            bigger_num = max(pair)
            return [sum_of_num - (bigger_num - 1), sum_of_num, sum_of_num + (limit - smaller_num)]

        def fill_default_dict(target_dict, key):
            if target_dict[key]:
                target_dict[key][0] += 1
            else:
                target_dict[key] = [1]
            return target_dict

        total_length = len(nums)
        small_num_dict = defaultdict(list)
        sum_dict = defaultdict(list)
        bigger_num_dict = defaultdict(list)
        for i in range(total_length // 2):
            lower, sum_of_pair, upper = get_range([nums[i], nums[-i - 1]])
            sum_dict = fill_default_dict(sum_dict, sum_of_pair)
            small_num_dict = fill_default_dict(small_num_dict, lower)
            bigger_num_dict = fill_default_dict(bigger_num_dict, upper)

        # print(small_num_dict)
        # print(sum_dict)
        # print(bigger_num_dict)
        max_count = 0
        count = 0
        for j in range(2 * limit + 2):
            if j in small_num_dict:
                count += small_num_dict[j][0]
            if j - 1 in bigger_num_dict:
                count -= bigger_num_dict[j - 1][0]
            if j in sum_dict:
                if max_count < count + sum_dict[j][0]:
                    max_count = count + sum_dict[j][0]
            else:
                if max_count < count:
                    max_count = count
            # print(f"{j}th step: max_count = {max_count}, count = {count}")

        return total_length - max_count


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1674.py")])
