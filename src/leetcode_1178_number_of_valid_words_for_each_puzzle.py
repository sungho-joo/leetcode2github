# @l2g 1178 python3
# [1178] Number of Valid Words for Each Puzzle
# Difficulty: Hard
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle
#
# With respect to a given puzzle string,
# a word is valid if both the following conditions are satisfied:
#
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
#
# For example,if the puzzle is "abcdefg",then valid words are "faced","cabbage",and "baggage",while
# invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
#
#
#
# Return an array answer,
# where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].
#
# Example 1:
#
# Input: words = ["aaaa","asas","able","ability","actt","actor","access"],puzzles = ["aboveyz",
# "abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa"
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
#
# Example 2:
#
# Input: words = ["apple","pleas","please"],puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy",
# "xaelpsy"]
# Output: [0,1,3,2,0]
#
#
# Constraints:
#
# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i] and puzzles[i] consist of lowercase English letters.
# Each puzzles[i] does not contain repeated characters.
#
#

import itertools
from typing import Counter, List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        #         class Trie:
        #             def __init__(self):
        #                 self.trie = dict()

        #             def insert(self, alp):
        #                 ind = 0
        #                 trie = self.trie
        #                 while ind < len(alp):
        #                     if alp[ind] in trie:
        #                         if ind == (len(alp) - 1): trie[alp[ind]][0] += 1
        #                         trie = trie[alp[ind]][1]
        #                     else:
        #                         trie[alp[ind]] = [0, dict()]
        #                         if ind == (len(alp) - 1): trie[alp[ind]][0] += 1
        #                         trie = trie[alp[ind]][1]
        #                     ind += 1

        #             def search_puzzle(self, alp, first_alp):
        #                 ind = 0
        #                 trie = self.trie
        #                 ans = 0
        #                 is_found = False
        #                 while ind < len(alp):
        #                     if alp[ind] in trie:
        #                         trie = trie[alp[ind]][1]
        #                     else:
        #                         ind += 1
        #                     ind += 1

        def get_mask(word):
            mask = 0
            for alp in iter(word):
                mask += 1 << (ord(alp) - ord("a"))
            return mask

        word_set = [set(word) for word in words]
        word_mask = []
        for word in word_set:
            word_mask.append(get_mask(word))
        # puzzle_mask = get_masks(puzzles)

        word_count = Counter(word_mask)

        ans = []
        for i in range(len(puzzles)):
            cnt = 0
            for k in range(7):
                for c in itertools.combinations(puzzles[i][1:], k):
                    mask = get_mask(tuple(puzzles[i][0]) + c)
                    cnt += word_count.get(mask, 0)
            ans.append(cnt)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1178.py")])
