# @l2g 212 python3
# [212] Word Search II
# Difficulty: Hard
# https://leetcode.com/problems/word-search-ii
#
# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.trie = defaultdict(dict)

            def insert(self, string):
                trie = self.trie
                for i in range(len(string)):
                    if string[i] in trie:
                        trie = trie[string[i]]
                    else:
                        trie[string[i]] = dict()
                        trie = trie[string[i]]
                trie["#"] = "#"

        word_trie = Trie()
        for word in iter(set(words)):
            word_trie.insert(word)

        n, m = len(board), len(board[0])
        boundary_checker = lambda x, y: 0 <= x < n and 0 <= y < m
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ans = []

        def dfs(x, y, arr, next_dict):
            # Base case
            if "#" in next_dict:
                next_dict.pop("#")
                ans.append("".join(arr))

            if len(next_dict) == 0:
                return

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if boundary_checker(nx, ny) and board[nx][ny] != -1 and board[nx][ny] in next_dict:
                    temp = board[nx][ny]
                    board[nx][ny] = -1
                    dfs(nx, ny, arr + [temp], next_dict[temp])
                    board[nx][ny] = temp

        for i in range(n):
            for j in range(m):
                ori = board[i][j]
                board[i][j] = -1
                dfs(i, j, [ori], word_trie.trie[ori])
                board[i][j] = ori

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_212.py")])
