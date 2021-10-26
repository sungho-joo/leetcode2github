# @l2g 543 python3
# [543] Diameter of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/diameter-of-binary-tree
#
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Example 2:
#
# Input: root = [1,2]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 10^4].
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Traverse with postorder and get maximum depth of each subtree
        # Each root gets maximum depth of each subtree, get maximum of each sum

        ans = [-float("inf")]

        def traverse(root):
            if not root:
                return -1

            left_depth = traverse(root.left) + 1
            right_depth = traverse(root.right) + 1
            ans[0] = max(ans[0], left_depth + right_depth)
            return max(left_depth, right_depth)

        _ = traverse(root)
        return ans[0]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_543.py")])
