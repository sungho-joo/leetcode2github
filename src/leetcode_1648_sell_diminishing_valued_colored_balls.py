# @l2g 1648 python3
# [1648] Sell Diminishing-Valued Colored Balls
# Difficulty: Medium
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls
#
# You have an inventory of different colored balls,
# and there is a customer that wants orders balls of any color.
# The customer weirdly values the colored balls.
# Each colored ball's value is the number of balls of that color you currently have in your inventory.
# For example,if you own 6 yellow balls,the customer would pay 6 for the first yellow ball.
# After the transaction,there are only 5 yellow balls left,
# so the next yellow ball is then valued at 5 (i.e.,
# the value of the balls decreases as you sell more to the customer).
# You are given an integer array,inventory,
# where inventory[i] represents the number of balls of the ith color that you initially own.
# You are also given an integer orders,
# which represents the total number of balls that the customer wants.
# You can sell the balls in any order.
# Return the maximum total value that you can attain after selling orders colored balls.
# As the answer may be too large,return it modulo 109 + 7.
#
# Example 1:
#
#
# Input: inventory = [2,5], orders = 4
# Output: 14
# Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
# The maximum total value is 2 + 5 + 4 + 3 = 14.
#
# Example 2:
#
# Input: inventory = [3,5], orders = 6
# Output: 19
# Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
# The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
#
# Example 3:
#
# Input: inventory = [2,8,4,10,6], orders = 20
# Output: 110
#
# Example 4:
#
# Input: inventory = [1000000000], orders = 1000000000
# Output: 21
# Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000.
# 500000000500000000 modulo 109 + 7 = 21.
#
#
# Constraints:
#
# 1 <= inventory.length <= 10^5
# 1 <= inventory[i] <= 10^9
# 1 <= orders <= min(sum(inventory[i]), 10^9)
#
#

from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def isometric_sequence(start, end, iso_length):
            res = int(iso_length * (start + end) // 2)
            return res

        def get_score_order_invetory(orders, inventory, overlaps):
            if orders >= overlaps * (inventory[0] - inventory[overlaps]):
                # Case 1 : Orders > overlaps * (inventory[0] - inventory[overlaps])
                # -> reduce as much as possible with current overlaps
                # Get score_increment
                iso_length = inventory[0] - inventory[overlaps]
                score_increment = isometric_sequence(
                    inventory[0],
                    inventory[overlaps] + 1,
                    iso_length,
                )
                score_increment *= overlaps

                # Update orders
                orders -= overlaps * iso_length

                # Update inventory
                for i in range(overlaps):
                    inventory[i] = int(inventory[overlaps])

                return orders, score_increment, inventory
            else:
                # Case 2 : Orders < overlaps * (inventory[0] - inventory[overlaps])
                # -> reduce till order reaches 0
                # Get score_increment
                iso_length = orders // overlaps
                remainder = orders % overlaps
                score_increment = isometric_sequence(
                    inventory[0],
                    inventory[0] - iso_length + 1,
                    iso_length,
                )
                score_increment *= overlaps
                score_increment += (inventory[0] - iso_length) * remainder

                # Update orders
                orders = 0

                # Update inventory not needed

                return orders, score_increment, inventory

        def find_overlaps(inventory):
            """Find count of colors that has same number as biggest number"""
            cur_num = inventory[0]
            i = 1
            while i < len(inventory):
                if cur_num != inventory[i]:
                    break
                else:
                    i += 1
            return i

        inventory = sorted(inventory, reverse=True)
        inventory = inventory + [0]

        score = 0
        while orders > 0:
            overlaps = find_overlaps(inventory)
            orders, score_increment, inventory = get_score_order_invetory(orders, inventory, overlaps)
            score += score_increment

        ans = score % (10 ** 9 + 7)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1648.py")])
