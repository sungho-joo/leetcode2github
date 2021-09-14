# @l2g 108 python3
# [108] Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
#
#
# Constraints:
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
#
#

from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dp(l, r):
            if l >= r:
                return
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = dp(l, mid)
            root.right = dp(mid + 1, r)
            return root

        return dp(0, len(nums))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_108.py")])
