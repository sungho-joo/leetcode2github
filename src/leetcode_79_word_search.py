# @l2g 79 python3
# [79] Word Search
# Difficulty: Medium
# https://leetcode.com/problems/word-search
#
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
# Follow up: Could you use search pruning to make your solution faster with a larger board?
#

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m

        def dfs(idx, x, y):
            if not boundary_checker(x, y) or board[x][y] == "#":
                return False
            if board[x][y] != word[idx]:
                return False
            if idx == len(word) - 1 and board[x][y] == word[idx]:
                return True

            tmp = board[x][y]
            board[x][y] = "#"
            res = (
                dfs(idx + 1, x + 1, y)
                or dfs(idx + 1, x - 1, y)
                or dfs(idx + 1, x, y + 1)
                or dfs(idx + 1, x, y - 1)
            )
            board[x][y] = tmp
            return res

        for i in range(n):
            for j in range(m):
                if dfs(0, i, j):
                    return True
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_79.py")])
