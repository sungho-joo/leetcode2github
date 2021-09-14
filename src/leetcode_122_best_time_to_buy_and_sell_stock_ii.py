# @l2g 122 python3
# [122] Best Time to Buy and Sell Stock II
# Difficulty: Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day,you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.However,
# you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
#
# Example 2:
#
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
#
# Example 3:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit,
# so we never buy the stock to achieve the maximum profit of 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
#
#

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for price in prices:
            if not stack:
                stack.append(price)

            if len(stack) == 1:
                if stack[-1] > price:
                    stack[0] = price
                elif stack[-1] < price:
                    stack.append(price)

            if len(stack) == 2:
                if stack[-1] < price:
                    stack[1] = price
                elif stack[-1] > price:
                    ans += stack[1] - stack[0]
                    stack = [price]

        if len(stack) == 2:
            ans += stack[1] - stack[0]
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_122.py")])
