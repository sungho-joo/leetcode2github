# @l2g 328 python3
# [328] Odd Even Linked List
# Difficulty: Medium
# https://leetcode.com/problems/odd-even-linked-list
#
# Given the head of a singly linked list,
# group all the nodes with odd indices together followed by the nodes with even indices,
# and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
# Constraints:
#
# n == number of nodes in the linked list
# 0 <= n <= 10^4
# -10^6 <= Node.val <= 10^6
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd_node = head
        even_node = even_head = head.next

        while (odd_node and odd_node.next) and (even_node and even_node.next):
            odd_node.next = odd_node.next.next
            even_node.next = even_node.next.next
            odd_node = odd_node.next
            even_node = even_node.next

        odd_node.next = even_head

        return head


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_328.py")])
