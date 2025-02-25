# @l2g 206 python3
# [206] Reverse Linked List
# Difficulty: Easy
# https://leetcode.com/problems/reverse-linked-list
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.Could you implement both?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_206.py")])
