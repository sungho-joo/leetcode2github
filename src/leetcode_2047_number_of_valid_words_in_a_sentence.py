# @l2g 2047 python3
# [2047] Number of Valid Words in a Sentence
# Difficulty: Easy
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence
#
# A sentence consists of lowercase letters ('a' to 'z'),digits ('0' to '9'),hyphens ('-'),
# punctuation marks ('!','.',and ','),and spaces (' ') only.
# Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.
# A token is a valid word if:
#
# It only contains lowercase letters, hyphens, and/or punctuation (no digits).
# There is at most one hyphen '-'.If present,
# it should be surrounded by lowercase characters ("a-b" is valid,but "-ab" and "ab-" are not valid).
# There is at most one punctuation mark. If present, it should be at the end of the token.
#
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
# Given a string sentence, return the number of valid words in sentence.
#
# Example 1:
#
# Input: sentence = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".
#
# Example 2:
#
# Input: sentence = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.
#
# Example 3:
#
# Input: sentence = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
# "stone-game10" is invalid because it contains digits.
#
# Example 4:
#
# Input: sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
# Output: 6
# Explanation: The valid words in the sentence are "he","bought","pencils,","erasers,","and",
# and "pencil-sharpener.".
#
#
# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
# There will be at least 1 token.
#
#


class Solution:
    def countValidWords(self, sentence: str) -> int:
        arr = sentence.split()

        def check_validity(s):
            hyp_count = 0
            punc_count = 0
            for i, alp in enumerate(s):
                if alp.isdecimal():
                    return False
                if alp == "-":
                    if hyp_count != 0:
                        return False
                    hyp_count += 1
                    if 0 < i < (len(s) - 1) and s[i - 1].isalpha and s[i + 1].isalpha():
                        pass
                    else:
                        return False
                if alp in [".", ",", "!"]:
                    if punc_count != 0:
                        return False
                    if i != (len(s) - 1):
                        return False
                    punc_count += 1
            return True

        token_count = 0
        for s in arr:
            if check_validity(s):
                token_count += 1

        return token_count


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2047.py")])
