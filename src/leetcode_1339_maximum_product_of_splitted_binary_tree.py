# @l2g 1339 python3
# [1339] Maximum Product of Splitted Binary Tree
# Difficulty: Medium
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree
#
# Given the root of a binary tree,
# split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees.Since the answer may be too large,
# return it modulo 10^9 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10.
# Their product is 110 (11*10)
#
# Example 2:
#
#
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
#
# Example 3:
#
# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
#
# Example 4:
#
# Input: root = [1,1]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 5 * 10^4].
# 1 <= Node.val <= 10^4
#
#

from typing import Optional


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sum = []

        def traverse(root):
            if not root:
                return 0

            cur_sum = root.val
            left_sum = traverse(root.left) if root.left else 0

            cur_sum += left_sum
            tree_sum.append(left_sum)

            right_sum = traverse(root.right) if root.right else 0

            cur_sum += right_sum
            tree_sum.append(right_sum)
            return cur_sum

        total_sum = traverse(root)
        ans = 0
        for i in range(len(tree_sum)):
            ans = max(ans, (total_sum - tree_sum[i]) * tree_sum[i])
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1339.py")])
