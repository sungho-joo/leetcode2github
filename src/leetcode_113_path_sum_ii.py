# @l2g 113 python3
# [113] Path Sum II
# Difficulty: Medium
# https://leetcode.com/problems/path-sum-ii
#
# Given the root of a binary tree and an integer targetSum,
# return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values,not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node.
# A leaf is a node with no children.
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []

        def traverse(root, path, path_sum):
            if path_sum == targetSum and not root.left and not root.right:
                ans.append(path)
            if root.left:
                traverse(root.left, path + [root.left.val], path_sum + root.left.val)
            if root.right:
                traverse(root.right, path + [root.right.val], path_sum + root.right.val)

        if root:
            traverse(root, [root.val], root.val)

        return ans if ans else []


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_113.py")])
