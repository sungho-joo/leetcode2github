# @l2g 101 python3
# [101] Symmetric Tree
# Difficulty: Easy
# https://leetcode.com/problems/symmetric-tree
#
# Given the root of a binary tree,check whether it is a mirror of itself (i.e.,
# symmetric around its center).
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
# Follow up: Could you solve it both recursively and iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append((root.left, root.right))

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue

            if not (left and right):
                return False
            if left.val != right.val:
                return False

            queue.extend([(left.left, right.right), (left.right, right.left)])

        return True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_101.py")])
