# @l2g 331 python3
# [331] Verify Preorder Serialization of a Binary Tree
# Difficulty: Medium
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree
#
# One way to serialize a binary tree is to use preorder traversal.When we encounter a non-null node,
# we record the node's value.If it is a null node,we record using a sentinel value such as '#'.
#
# For example,the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
# where '#' represents a null node.
# Given a string of comma-separated values preorder,
# return true if it is a correct preorder traversal serialization of a binary tree.
# It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
# You may assume that the input format is always valid.
#
# For example, it could never contain two consecutive commas, such as "1,,3".
#
# Note: You are not allowed to reconstruct the tree.
#
# Example 1:
# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# Example 2:
# Input: preorder = "1,#"
# Output: false
# Example 3:
# Input: preorder = "9,#,#,1"
# Output: false
#
#
# Constraints:
#
# 1 <= preorder.length <= 10^4
# preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
#
#


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # rule 1 : ab = b is left child of a
        # rule 2 : a#c : # is left child of a, c is right child
        # how to solve? keep track of parent stack and remove them.

        parent = 1 if preorder[0] != "#" else 0
        prev = preorder[0]
        for num in preorder.split(",")[1:]:
            if parent == 0:
                return False

            # Case 1 : prev is number
            if prev != "#":
                # Add left node
                if num != "#":
                    parent += 1
            # Case2 : prev is #
            else:
                parent -= 1
                if num != "#":
                    parent += 1

            prev = num

        return False if parent else True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_331.py")])
