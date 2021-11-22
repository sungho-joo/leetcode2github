# @l2g 96 python3
# [96] Unique Binary Search Trees
# Difficulty: Medium
# https://leetcode.com/problems/unique-binary-search-trees
#
# Given an integer n,
# return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 19
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def traverse(length):
            # base case
            if length <= 0:
                return 0
            if length == 1:
                return 1

            ans = 0
            for i in range(length):
                left_cnt = traverse(i)
                right_cnt = traverse(length - i - 1)
                if left_cnt and right_cnt:
                    ans += left_cnt * right_cnt
                else:
                    ans += left_cnt + right_cnt
            return ans

        return traverse(n)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_96.py")])
