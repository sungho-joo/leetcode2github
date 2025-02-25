# @l2g 94 python3
# [94] Binary Tree Inorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal
#
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Example 2:
#
# Input: root = []
# Output: []
#
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
#
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        ans, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_94.py")])
