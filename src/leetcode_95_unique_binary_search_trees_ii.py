# @l2g 95 python3
# [95] Unique Binary Search Trees II
# Difficulty: Medium
# https://leetcode.com/problems/unique-binary-search-trees-ii
#
# Given an integer n,return all the structurally unique BST's (binary search trees),
# which has exactly n nodes of unique values from 1 to n.Return the answer in any order.
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
# Example 2:
#
# Input: n = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= n <= 8
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return [None]
            ans = []
            for i in range(l, r + 1):
                all_left_subtrees = dp(l, i - 1)
                all_right_subtrees = dp(i + 1, r)

                for left_subtree in all_left_subtrees:
                    for right_subtree in all_right_subtrees:
                        node = TreeNode(i, left_subtree, right_subtree)
                        ans.append(node)
            return ans

        return dp(1, n)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_95.py")])
