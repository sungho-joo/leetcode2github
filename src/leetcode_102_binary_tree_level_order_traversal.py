# @l2g 102 python3
# [102] Binary Tree Level Order Traversal
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal
#
# Given the root of a binary tree,return the level order traversal of its nodes' values.(i.e.,
# from left to right,level by level).
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            layer = []
            for _ in range(len(q)):
                node = q.popleft()
                layer.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(layer)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_102.py")])
