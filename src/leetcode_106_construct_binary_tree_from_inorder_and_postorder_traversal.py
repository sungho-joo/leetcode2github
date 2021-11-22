# @l2g 106 python3
# [106] Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
#
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree,
# construct and return the binary tree.
#
# Example 1:
#
#
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
#
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#
#
# Constraints:
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = defaultdict(list)
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.post_idx = len(postorder) - 1

        def traverse(l, r):
            # base case
            if l > r:
                return

            cur_value = postorder[self.post_idx]
            self.post_idx -= 1
            cur_node = TreeNode(val=cur_value)

            inorder_idx = inorder_map[cur_value]
            # right subtree
            cur_node.right = traverse(inorder_idx + 1, r)
            # left subtree
            cur_node.left = traverse(l, inorder_idx - 1)

            return cur_node

        return traverse(0, len(inorder) - 1)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_106.py")])
