# @l2g 105 python3
# [105] Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
#
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
# construct and return the binary tree.
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
# Constraints:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_dict = defaultdict(int)
        for i, v in enumerate(inorder):
            in_dict[v] = i

        self.pre_idx = 0

        def traverse(l, r):
            if l > r:
                return
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)

            self.pre_idx += 1

            root_idx = in_dict[root_val]
            root.left = traverse(l, root_idx - 1)
            root.right = traverse(root_idx + 1, r)
            return root

        return traverse(0, len(inorder) - 1)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_105.py")])
