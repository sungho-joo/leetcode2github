# @l2g 404 python3
# [404] Sum of Left Leaves
# Difficulty: Easy
# https://leetcode.com/problems/sum-of-left-leaves
#
# Given the root of a binary tree, return the sum of all left leaves.
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
#
# Example 2:
#
# Input: root = [1]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def traverse(root):
            if not root:
                return

            if root.left and not root.left.left and not root.left.right:
                self.ans += root.left.val
            traverse(root.left)
            traverse(root.right)

        traverse(root)

        return self.ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_404.py")])
