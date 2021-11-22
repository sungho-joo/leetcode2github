# @l2g 2055 python3
# [2055] Plates Between Candles
# Difficulty: Medium
# https://leetcode.com/problems/plates-between-candles
#
# There is a long table with a line of plates and candles arranged on top of it.
# You are given a 0-indexed string s consisting of characters '*' and '|' only,
# where a '*' represents a plate and a '|' represents a candle.
# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti,
# righti] denotes the substring s[lefti...righti] (inclusive).For each query,
# you need to find the number of plates between candles that are in the substring.
# A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.
#
# For example,s = "||**||**|*",and a query [3,8] denotes the substring "*||**|".
# The number of plates between candles in this substring is 2,
# as each of the two plates has at least one candle in the substring to its left and right.
#
# Return an integer array answer where answer[i] is the answer to the ith query.
#
# Example 1:
#
#
# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.
#
# Example 2:
#
#
# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.
#
#
# Constraints:
#
# 3 <= s.length <= 10^5
# s consists of '*' and '|' characters.
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= lefti <= righti < s.length
#
#

from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # for each candle, how many plates are on its left
        candle_map = defaultdict(int)
        plate_count = 0
        for i, elem in enumerate(s):
            if elem == "*":
                plate_count += 1
            else:
                candle_map[i] = plate_count

        # closest candle on its left, right (two pass)
        left_pass = [0] * len(s)
        right_pass = [0] * len(s)

        close_candle = -1
        for i, elem in enumerate(s):
            if elem == "|":
                close_candle = i
            left_pass[i] = close_candle

        close_candle = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "|":
                close_candle = i
            right_pass[i] = close_candle

        ans = []
        for s, e in queries:
            right_candle = left_pass[e]
            left_candle = right_pass[s]
            if right_candle == -1 or left_candle == -1 or left_candle >= right_candle:
                ans.append(0)
            else:
                plate_cnt = candle_map[right_candle] - candle_map[left_candle]
                ans.append(plate_cnt)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2055.py")])
