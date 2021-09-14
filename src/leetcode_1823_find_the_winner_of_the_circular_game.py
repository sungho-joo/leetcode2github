# @l2g 1823 python3
# [1823] Find the Winner of the Circular Game
# Difficulty: Medium
# https://leetcode.com/problems/find-the-winner-of-the-circular-game
#
# There are n friends that are playing a game.
# The friends are sitting in a circle and are numbered from 1 to n in clockwise order.More formally,
# moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n,
# and moving clockwise from the nth friend brings you to the 1st friend.
# The rules of the game are as follows:
#
# Start at the 1st friend.
# Count the next k friends in the clockwise direction including the friend you started at.
# The counting wraps around the circle and may count some friends more than once.
# The last friend you counted leaves the circle and loses the game.
# If there is still more than one friend in the circle,
# go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
# Else, the last friend in the circle wins the game.
#
# Given the number of friends, n, and an integer k, return the winner of the game.
#
# Example 1:
#
#
# Input: n = 5, k = 2
# Output: 3
# Explanation: Here are the steps of the game:
# 1) Start at friend 1.
# 2) Count 2 friends clockwise, which are friends 1 and 2.
# 3) Friend 2 leaves the circle. Next start is friend 3.
# 4) Count 2 friends clockwise, which are friends 3 and 4.
# 5) Friend 4 leaves the circle. Next start is friend 5.
# 6) Count 2 friends clockwise, which are friends 5 and 1.
# 7) Friend 1 leaves the circle. Next start is friend 3.
# 8) Count 2 friends clockwise, which are friends 3 and 5.
# 9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
# Example 2:
#
# Input: n = 6, k = 5
# Output: 1
# Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
#
#
# Constraints:
#
# 1 <= k <= n <= 500
#


class node:
    def __init__(self, id, prev_node=None, next_node=None):
        self.pos = id
        self.next = next_node
        self.prev = prev_node


class slinkedlist:
    def __init__(self):
        self.head = None


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        linked_list = slinkedlist()
        linked_list.head = node(1)
        cur_node = linked_list.head
        for i in range(1, n):
            cur_node.next = node(i + 1)
            cur_node.next.prev = cur_node
            cur_node = cur_node.next
        cur_node.next = linked_list.head
        linked_list.head.prev = cur_node

        start_node = linked_list.head

        while True:
            start_node = self.pop_node(k, start_node)

            if start_node.next == start_node:
                break
        return start_node.pos

    def pop_node(self, k, start_node):
        iter = 0
        prev_node = start_node
        # print('start node', start_node.pos)

        while iter < k - 1:
            cur_node = prev_node.next
            prev_node = cur_node
            iter += 1

        prev_node.next.prev = prev_node.prev
        prev_node.prev.next = prev_node.next
        # print(cur_node.pos)
        # print(cur_node.prev.pos)
        # print(cur_node.next.pos)

        return prev_node.next


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1823.py")])
