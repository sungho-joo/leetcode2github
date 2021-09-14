# @l2g 814 python3
# [814] Binary Tree Pruning
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-pruning
#
# Given the root of a binary tree,
# return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# A subtree of a node node is node plus every node that is a descendant of node.
#
# Example 1:
#
#
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
# Example 2:
#
#
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
# Example 3:
#
#
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def tree_traversal(root):
            if not root:
                return False

            tree_with_one = False
            if root.val == 1:
                tree_with_one = True

            if tree_traversal(root.left):
                tree_with_one = True
            else:
                root.left = None

            if tree_traversal(root.right):
                tree_with_one = True
            else:
                root.right = None

            return tree_with_one

        if tree_traversal(root):
            return root
        else:
            return


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_814.py")])
