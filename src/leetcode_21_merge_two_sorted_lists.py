# @l2g 21 python3
# [21] Merge Two Sorted Lists
# Difficulty: Easy
# https://leetcode.com/problems/merge-two-sorted-lists
#
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
#
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = head = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return head.next


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_21.py")])
