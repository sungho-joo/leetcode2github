# @l2g 725 python3
# [725] Split Linked List in Parts
# Difficulty: Medium
# https://leetcode.com/problems/split-linked-list-in-parts
#
# Given the head of a singly linked list and an integer k,
# split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one.
# This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list,
# and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.
#
# Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1,
# and earlier parts are a larger size than the later parts.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
#
#

from typing import List, Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total_node = 0
        temp = head
        while temp:
            temp = temp.next
            total_node += 1

        equal_steps, rem = divmod(total_node, k)
        ans = []
        for i in range(k):
            # print(i, head)
            node = ListNode(head.val) if head else None
            temp = node
            steps = equal_steps + (i < rem)
            while steps > 1 and head:
                temp.next = ListNode(head.next.val)
                temp = temp.next
                head = head.next
                steps -= 1
            if head:
                head = head.next
            ans.append(node)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_725.py")])
