# @l2g 843 python3
# [843] Guess the Word
# Difficulty: Hard
# https://leetcode.com/problems/guess-the-word
#
# This is an interactive problem.
# You are given an array of unique strings wordlist where wordlist[i] is 6 letters long,
# and one word in this list is chosen as secret.
# You may call Master.guess(word) to guess a word.
# The guessed word should have type string and must be from the original list with 6 lowercase letters.
# This function returns an integer type,
# representing the number of exact matches (value and position) of your guess to the secret word.Also,
# if your guess is not in the given wordlist,it will return -1 instead.
# For each test case,you have exactly 10 guesses to guess the word.At the end of any number of calls,
# if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret,
# then you pass the test case.
#
# Example 1:
#
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
# Output: You guessed the secret word correctly.
# Explanation:
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
#
# Example 2:
#
# Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
# Output: You guessed the secret word correctly.
#
#
# Constraints:
#
# 1 <= wordlist.length <= 100
# wordlist[i].length == 6
# wordlist[i] consist of lowercase English letters.
# All the strings of wordlist are unique.
# secret exists in wordlist.
# numguesses == 10
#
#


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random
from typing import List


class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        def filter_impossible_words(word, expected_match, candi_list):
            filtered_words = []

            for candi in candi_list:
                num_of_match = sum(word[k] == candi[k] for k in range(6))
                if num_of_match == expected_match:
                    filtered_words.append(candi)
            return filtered_words

        for _ in range(10):
            # random word choice
            word = random.choice(wordlist)
            num_of_match = master.guess(word)
            if num_of_match == 6:
                return
            wordlist = filter_impossible_words(word, num_of_match, wordlist)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_843.py")])
