# @l2g 104 python3
# [104] Maximum Depth of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree
#
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
#
# Input: root = [1,null,2]
# Output: 2
#
# Example 3:
#
# Input: root = []
# Output: 0
#
# Example 4:
#
# Input: root = [0]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return 0

            return max(traverse(root.left), traverse(root.right)) + 1

        return traverse(root)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_104.py")])
