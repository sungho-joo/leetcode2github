# @l2g 2049 python3
# [2049] Count Nodes With the Highest Score
# Difficulty: Medium
# https://leetcode.com/problems/count-nodes-with-the-highest-score
#
# There is a binary tree rooted at 0 consisting of n nodes.The nodes are labeled from 0 to n - 1.
# You are given a 0-indexed integer array parents representing the tree,
# where parents[i] is the parent of node i.Since node 0 is the root,parents[0] == -1.
# Each node has a score.To find the score of a node,
# consider if the node and the edges connected to it were removed.
# The tree would become one or more non-empty subtrees.
# The size of a subtree is the number of the nodes in it.
# The score of the node is the product of the sizes of all those subtrees.
# Return the number of nodes that have the highest score.
#
# Example 1:
#
#
# Input: parents = [-1,2,0,2,0]
# Output: 3
# Explanation:
# - The score of node 0 is: 3 * 1 = 3
# - The score of node 1 is: 4 = 4
# - The score of node 2 is: 1 * 1 * 2 = 2
# - The score of node 3 is: 4 = 4
# - The score of node 4 is: 4 = 4
# The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
#
# Example 2:
#
#
# Input: parents = [-1,2,0]
# Output: 2
# Explanation:
# - The score of node 0 is: 2 = 2
# - The score of node 1 is: 2 = 2
# - The score of node 2 is: 1 * 1 = 1
# The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
#
#
# Constraints:
#
# n == parents.length
# 2 <= n <= 10^5
# parents[0] == -1
# 0 <= parents[i] <= n - 1 for i != 0
# parents represents a valid binary tree.
#
#

from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        node_map = defaultdict(list)
        for i, v in enumerate(parents):
            if v == -1:
                continue
            node_map[v].append(i)

        subtree_sizes = [0] * len(parents)

        # postorder
        def traverse(root_val):
            sizes = 0
            for next_node in node_map[root_val]:
                tree_size = traverse(next_node)
                sizes += tree_size
            subtree_sizes[root_val] = sizes + 1
            return sizes + 1

        _ = traverse(0)

        score_list = [0] * len(parents)

        for i in range(len(parents)):
            subtree_score = len(parents) - subtree_sizes[i] if i != 0 else 1
            for next_node in node_map[i]:
                subtree_score *= subtree_sizes[next_node]
            score_list[i] = subtree_score

        max_score = max(score_list)
        return sum(score == max_score for score in score_list)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2049.py")])
