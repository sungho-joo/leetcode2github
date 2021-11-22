# @l2g 1110 python3
# [1110] Delete Nodes And Return Forest
# Difficulty: Medium
# https://leetcode.com/problems/delete-nodes-and-return-forest
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete,
# we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest. You may return the result in any order.
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
# Example 2:
#
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
#
#
# Constraints:
#
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        del_set = set(to_delete)
        ans = []

        def traverse(root, is_parent_deleted):
            if not root:
                return True

            is_deleted = root.val in del_set
            if is_parent_deleted and not is_deleted:
                ans.append(root)

            if traverse(root.left, is_deleted):
                root.left = None

            if traverse(root.right, is_deleted):
                root.right = None

            return is_deleted

        traverse(root, True)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1110.py")])
