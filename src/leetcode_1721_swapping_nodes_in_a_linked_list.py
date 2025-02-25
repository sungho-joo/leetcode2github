# @l2g 1721 python3
# [1721] Swapping Nodes in a Linked List
# Difficulty: Medium
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list
#
# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
#
# Example 2:
#
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
#
# Example 3:
#
# Input: head = [1], k = 1
# Output: [1]
#
# Example 4:
#
# Input: head = [1,2], k = 1
# Output: [2,1]
#
# Example 5:
#
# Input: head = [1,2,3], k = 2
# Output: [1,2,3]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 10^5
# 0 <= Node.val <= 100
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        full_list = [head]

        while head.next:
            head = head.next
            full_list.append(head)

        list_len = len(full_list)
        full_list[k - 1].val, full_list[list_len - k].val = (
            full_list[list_len - k].val,
            full_list[k - 1].val,
        )
        return full_list[0]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1721.py")])
