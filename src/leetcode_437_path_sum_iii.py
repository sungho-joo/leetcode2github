# @l2g 437 python3
# [437] Path Sum III
# Difficulty: Medium
# https://leetcode.com/problems/path-sum-iii
#
# Given the root of a binary tree and an integer targetSum,
# return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf,but it must go downwards (i.e.,
# traveling only from parent nodes to child nodes).
#
# Example 1:
#
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
# Example 2:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.ans = 0

        def traverse(root):
            if not root:
                return dict()

            ret = defaultdict(int)
            # only current node
            ret[root.val] += 1
            if root.val == targetSum:
                self.ans += 1

            # include current node
            left_sums = traverse(root.left)
            right_sums = traverse(root.right)

            for l_key, value in left_sums.items():
                left_sum = root.val + l_key
                if left_sum == targetSum:
                    self.ans += value
                ret[left_sum] += value

            for r_key, value in right_sums.items():
                right_sum = root.val + r_key
                if right_sum == targetSum:
                    self.ans += value
                ret[right_sum] += value
            return ret

        traverse(root)
        return self.ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_437.py")])
