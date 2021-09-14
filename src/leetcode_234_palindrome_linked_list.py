# @l2g 234 python3
# [234] Palindrome Linked List
# Difficulty: Easy
# https://leetcode.com/problems/palindrome-linked-list
#
# Given the head of a singly linked list, return true if it is a palindrome.
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
# Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid point
        # 1. loop til end
        # 2. two pointer (slow and fast)
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        reverse_node = slow
        # reverse linked list
        prev = None
        while reverse_node:
            temp = reverse_node
            reverse_node = reverse_node.next
            temp.next = prev
            prev = temp

        while prev and head:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_234.py")])
