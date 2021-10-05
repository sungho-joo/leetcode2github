# @l2g 572 python3
# [572] Subtree of Another Tree
# Difficulty: Easy
# https://leetcode.com/problems/subtree-of-another-tree
#
# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree_list = []

        def traverse(root):
            if not root:
                return
            if root.val == subRoot.val:
                tree_list.append(root)

            traverse(root.left)
            traverse(root.right)

        traverse(root)

        def co_traverse(root, subroot):
            # if one of node is none
            if not (root and subroot):
                return root is subroot

            # if values are different
            if root.val != subroot.val:
                return False

            return co_traverse(root.left, subroot.left) and co_traverse(root.right, subroot.right)

        return any(co_traverse(node, subRoot) for node in tree_list)


# 1. traverse root tree
# 2. find node that has same value as subroot
# 3. if found, append node to list
# 4. traverse with root


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_572.py")])
