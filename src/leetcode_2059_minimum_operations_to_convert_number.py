# @l2g 2059 python3
# [2059] Minimum Operations to Convert Number
# Difficulty: Medium
# https://leetcode.com/problems/minimum-operations-to-convert-number
#
# You are given a 0-indexed integer array nums containing distinct numbers,an integer start,
# and an integer goal.There is an integer x that is initially set to start,
# and you want to perform operations on x such that it is converted to goal.
# You can perform the following operation repeatedly on the number x:
# If 0 <= x <= 1000,then for any index i in the array (0 <= i < nums.length),
# you can set x to any of the following:
#
# x + nums[i]
# x - nums[i]
# x ^ nums[i] (bitwise-XOR)
#
# Note that you can use each nums[i] any number of times in any order.
# Operations that set x to be out of the range 0 <= x <= 1000 are valid,
# but no more operations can be done afterward.
# Return the minimum number of operations needed to convert x = start into goal,
# and -1 if it is not possible.
#
# Example 1:
#
# Input: nums = [1,3], start = 6, goal = 4
# Output: 2
# Explanation:
# We can go from 6 → 7 → 4 with the following 2 operations.
# - 6 ^ 1 = 7
# - 7 ^ 3 = 4
#
# Example 2:
#
# Input: nums = [2,4,12], start = 2, goal = 12
# Output: 2
# Explanation:
# We can go from 2 → 14 → 12 with the following 2 operations.
# - 2 + 12 = 14
# - 14 - 2 = 12
#
# Example 3:
#
# Input: nums = [3,5,7], start = 0, goal = -4
# Output: 2
# Explanation:
# We can go from 0 → 3 → -4 with the following 2 operations.
# - 0 + 3 = 3
# - 3 - 7 = -4
# Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.
#
# Example 4:
#
# Input: nums = [2,8,16], start = 0, goal = 1
# Output: -1
# Explanation:
# There is no way to convert 0 into 1.
# Example 5:
#
# Input: nums = [1], start = 0, goal = 3
# Output: 3
# Explanation:
# We can go from 0 → 1 → 2 → 3 with the following 3 operations.
# - 0 + 1 = 1
# - 1 + 1 = 2
# - 2 + 1 = 3
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -10^9 <= nums[i], goal <= 10^9
# 0 <= start <= 1000
# start != goal
# All the integers in nums are distinct.
#
#

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = [0] * 1001
        visited[start] = 1

        q = deque()
        q.append([start, 0])

        while q:
            for _ in range(len(q)):
                cur_num, cnt = q.popleft()

                if cur_num == goal:
                    return cnt

                for num in nums:
                    # plus
                    p_num = cur_num + num
                    if p_num == goal:
                        return cnt + 1
                    if 0 <= p_num <= 1000 and visited[p_num] == 0:
                        q.append([p_num, cnt + 1])
                        visited[p_num] = 1
                    # minus
                    m_num = cur_num - num
                    if m_num == goal:
                        return cnt + 1
                    if 0 <= m_num <= 1000 and visited[m_num] == 0:
                        q.append([m_num, cnt + 1])
                        visited[m_num] = 1
                    # XOR
                    xor_num = cur_num ^ num
                    if xor_num == goal:
                        return cnt + 1
                    if 0 <= xor_num <= 1000 and visited[xor_num] == 0:
                        q.append([xor_num, cnt + 1])
                        visited[xor_num] = 1
        return -1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2059.py")])
