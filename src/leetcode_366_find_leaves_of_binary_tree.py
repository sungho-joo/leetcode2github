# @l2g 366 python3
# [366] Find Leaves of Binary Tree
# Difficulty: Medium
# https://leetcode.com/problems/find-leaves-of-binary-tree
#
# Given the root of a binary tree, collect a tree's nodes as if you were doing this:
#
# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],
# [1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
#
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def traverse(root):
            # returns list of nodes in subtree which are grouped by same layer(height)
            if not root:
                return -1

            left = traverse(root.left)
            right = traverse(root.right)
            height = max(left, right) + 1
            if height < len(ans):
                ans[height].append(root.val)
            else:
                ans.append([root.val])
            return height

        traverse(root)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_366.py")])
