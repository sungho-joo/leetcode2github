# @l2g 103 python3
# [103] Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
#
# Given the root of a binary tree,return the zigzag level order traversal of its nodes' values.(i.e.,
# from left to right,then right to left for the next level and alternate between).
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
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
# -100 <= Node.val <= 100
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        # BFS
        layer = [root]
        direction = 0
        # left->right : 0, right->left: 1
        ans = []
        while layer:
            new_layer, layer_ans = [], []
            for node in layer:
                layer_ans.append(node.val)
                children = []
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
                if direction == 1:
                    children.reverse()
                new_layer.extend(children)
            ans.append(layer_ans)
            new_layer.reverse()
            layer = new_layer
            direction ^= 1
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_103.py")])
