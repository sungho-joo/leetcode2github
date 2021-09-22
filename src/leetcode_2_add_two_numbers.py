# @l2g 2 python3
# [2] Add Two Numbers
# Difficulty: Medium
# https://leetcode.com/problems/add-two-numbers
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order,and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(sum_list, l1, l2=None, carry=0):
            if not l2:
                l2 = True
            while l1 and l2:
                total = l1.val + carry
                if not isinstance(l2, bool):
                    total += l2.val
                carry, val = divmod(total, 10)
                sum_list.next = ListNode(val)
                sum_list = sum_list.next
                l1 = l1.next
                if not isinstance(l2, bool):
                    l2 = l2.next
            return sum_list, l1, l2, carry

        head = sum_list = ListNode(0)
        sum_list, l1, l2, carry = traverse(sum_list, l1, l2)
        if l1:
            sum_list, l1, _, carry = traverse(sum_list, l1, carry=carry)
        if l2:
            sum_list, l2, _, carry = traverse(sum_list, l2, carry=carry)
        if carry:
            sum_list.next = ListNode(1)
        return head.next


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2.py")])
