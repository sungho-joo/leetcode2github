# @l2g 450 python3
# [450] Delete Node in a BST
# Difficulty: Medium
# https://leetcode.com/problems/delete-node-in-a-bst
#
# Given a root node reference of a BST and a key,delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
#
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
# Example 3:
#
# Input: root = [], key = 0
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5
#
#
# Follow up: Could you solve it with time complexity O(height of tree)?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def update_root(parent, root, lr):
            left, right = root.left, root.right
            # No children
            if not left and not right:
                if lr == 1:
                    parent.right = None
                if lr == 0:
                    parent.left = None
            # Only one child
            elif not (left and right):
                valid_node = left if left else right
                if lr == 1:
                    parent.right = valid_node
                if lr == 0:
                    parent.left = valid_node
            # Two children
            else:
                # get before (biggest number that is smaller than cur node)
                slow, fast = root, root.left
                while fast.right:
                    slow = fast
                    fast = fast.right
                # remove before node
                if slow is root:
                    update_root(slow, fast, 0)
                else:
                    update_root(slow, fast, 1)

                root.val = fast.val

        def traverse(prev, root, lr):
            # lr = 1 -> right child, lr = 0 -> left child
            if not root:
                return

            if root.val < key:
                traverse(root, root.right, 1)
            elif root.val > key:
                traverse(root, root.left, 0)
            else:
                update_root(prev, root, lr)

        pseudo_root = TreeNode(right=root)
        traverse(pseudo_root, root, 1)
        return pseudo_root.right


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_450.py")])
