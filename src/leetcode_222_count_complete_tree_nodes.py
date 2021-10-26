# @l2g 222 python3
# [222] Count Complete Tree Nodes
# Difficulty: Medium
# https://leetcode.com/problems/count-complete-tree-nodes
#
# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia,every level,except possibly the last,
# is completely filled in a complete binary tree,
# and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
# Example 2:
#
# Input: root = []
# Output: 0
#
# Example 3:
#
# Input: root = [1]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def subtree_left_check(root):
            height = 0
            while root:
                height += 1
                root = root.left

            return height

        def traverse(root):
            if not root:
                return 0
            left_height = subtree_left_check(root.left)
            right_height = subtree_left_check(root.right)

            if left_height == right_height:
                return pow(2, left_height) + traverse(root.right)
            else:
                return pow(2, right_height) + traverse(root.left)

        return traverse(root)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_222.py")])
