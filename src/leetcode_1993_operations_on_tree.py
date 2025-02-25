# @l2g 1993 python3
# [1993] Operations on Tree
# Difficulty: Medium
# https://leetcode.com/problems/operations-on-tree
#
# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node.
# The root of the tree is node 0,so parent[0] = -1 since it has no parent.
# You want to design a data structure that allows users to lock,unlock,and upgrade nodes in the tree.
# The data structure should support the following functions:
#
# Lock: Locks the given node for the given user and prevents other users from locking the same node.
# You may only lock a node if the node is unlocked.
# Unlock: Unlocks the given node for the given user.
# You may only unlock a node if it is currently locked by the same user.
# Upgrade: Locks the given node for the given user and unlocks all of its descendants.
# You may only upgrade a node if all 3 conditions are true:
#
# The node is unlocked,
# It has at least one locked descendant (by any user), and
# It does not have any locked ancestors.
#
#
#
# Implement the LockingTree class:
#
# LockingTree(int[] parent) initializes the data structure with the parent array.
# lock(int num,
# int user) returns true if it is possible for the user with id user to lock the node num,
# or false otherwise.If it is possible,the node num will become locked by the user with id user.
# unlock(int num,
# int user) returns true if it is possible for the user with id user to unlock the node num,
# or false otherwise.If it is possible,the node num will become unlocked.
# upgrade(int num,
# int user) returns true if it is possible for the user with id user to upgrade the node num,
# or false otherwise.If it is possible,the node num will be upgraded.
#
#
# Example 1:
#
#
# Input
# ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
# [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
# Output
# [null, true, false, true, true, true, false]
#
# Explanation
# LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
# lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
#                            // Node 2 will now be locked by user 2.
# lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
# lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
#                            // Node 2 will now be unlocked.
# lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
#                            // Node 4 will now be locked by user 5.
# lockingTree.upgrade(0,
# 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
#                            // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
# lockingTree.lock(0, 1);    // return false because node 0 is already locked.
#
#
# Constraints:
#
# n == parent.length
# 2 <= n <= 2000
# 0 <= parent[i] <= n - 1 for i != 0
# parent[0] == -1
# 0 <= num <= n - 1
# 1 <= user <= 10^4
# parent represents a valid tree.
# At most 2000 calls in total will be made to lock, unlock, and upgrade.
#
#

import collections
from typing import List


class LockingTree:
    def __init__(self, parent: List[int]):
        self.n = len(parent)
        self.parent = parent
        self.locked = [0] * len(parent)
        self.children = self.get_children()

    def get_children(self):
        children = collections.defaultdict(list)
        for c, p in enumerate(self.parent):
            children[p].append(c)
        return children

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # First case: if num is unlocked
        if self.locked[num] != 0:
            return False
        # Second case: if any ancestors are locked
        prev = num
        while prev != -1 and self.locked[prev] == 0:
            prev = self.parent[prev]
        if prev != -1:
            return False

        # Third case: if any decendants are locked
        self.is_locked = False

        def traverse(node):
            if self.children[node]:
                for next_num in self.children[node]:
                    traverse(next_num)

            if self.locked[node] != 0:
                self.is_locked = True
                self.locked[node] = 0

        traverse(num)
        if not self.is_locked:
            return False

        # Upgrade
        self.locked[num] = user
        self.is_locked = False
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1993.py")])
