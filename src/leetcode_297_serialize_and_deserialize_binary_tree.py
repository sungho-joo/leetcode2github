# @l2g 297 python3
# [297] Serialize and Deserialize Binary Tree
# Difficulty: Hard
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format,
# so please be creative and come up with different approaches yourself.
#
# Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
# Example 2:
#
# Input: root = []
# Output: []
#
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
# Example 4:
#
# Input: root = [1,2]
# Output: [1,2]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def traverse(root):
            if not root:
                ans.append("#")
                ans.append("[]")
                return

            ans.append(f"{root.val}")
            ans.append("[")
            traverse(root.left)
            traverse(root.right)
            ans.append("]")

        traverse(root)
        return "".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def find_mid(l, r):
            l_b, r_b = 0, 0
            for i in range(l + 1, r + 1):
                if data[i] == "[":
                    l_b += 1
                elif data[i] == "]":
                    r_b += 1
                else:
                    continue
                if l_b == r_b:
                    return i

        # print(data)
        def traverse(left, right):
            if right < left:
                return
            if right == left + 1:
                return
            if data[left] == "#":
                return

            val_ind = data[left:].index("[") + left
            val = data[left:val_ind]
            left = val_ind - 1
            root = TreeNode(val)
            subtree_range = find_mid(left, right)

            m = find_mid(left + 2, subtree_range - 1)
            root.left = traverse(left + 2, m)
            root.right = traverse(m + 1, subtree_range - 1)
            return root

        return traverse(0, len(data) - 1)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_297.py")])
