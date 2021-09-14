# @l2g 1871 python3
# [1871] Jump Game VII
# Difficulty: Medium
# https://leetcode.com/problems/jump-game-vii
#
# You are given a 0-indexed binary string s and two integers minJump and maxJump.In the beginning,
# you are standing at index 0,which is equal to '0'.
# You can move from index i to index j if the following conditions are fulfilled:
#
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
#
# Return true if you can reach index s.length - 1 in s, or false otherwise.
#
# Example 1:
#
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3.
# In the second step, move from index 3 to index 5.
#
# Example 2:
#
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
#
#
# Constraints:
#
# 2 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
#
#

import collections


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = collections.deque([0])
        max_index = 0
        while q:
            ind = q.popleft()
            if ind == len(s) - 1:
                return True
            start = max(max_index + 1, ind + minJump)
            for next_pos in range(start, min(ind + maxJump + 1, len(s))):
                if s[next_pos] == "0":
                    q.append(next_pos)
            max_index = ind + maxJump
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1871.py")])
