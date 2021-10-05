# @l2g 230 python3
# [230] Kth Smallest Element in a BST
# Difficulty: Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-bst
#
# Given the root of a binary search tree,and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
# Follow up: If the BST is modified often (i.e.,
# we can do insert and delete operations) and you need to find the kth smallest frequently,
# how would you optimize?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_th = k
        ans = [-1]

        def traverse(root):
            if not root:
                return
            if self.k_th <= 0:
                return

            traverse(root.left)
            self.k_th -= 1
            if self.k_th == 0:
                ans[0] = root.val
            traverse(root.right)

        traverse(root)
        return ans[0]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_230.py")])
