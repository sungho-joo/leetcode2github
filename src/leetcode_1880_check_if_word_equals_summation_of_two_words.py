# @l2g 1880 python3
# [1880] Check if Word Equals Summation of Two Words
# Difficulty: Easy
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words
#
# The letter value of a letter is its position in the alphabet starting from 0 (i.e.'a' -> 0,'b' -> 1,
# 'c' -> 2,etc.).
# The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s,
# which is then converted into an integer.
#
# For example,if s = "acb",we concatenate each letter's letter value,resulting in "021".
# After converting it,we get 21.
#
# You are given three strings firstWord,secondWord,and targetWord,
# each consisting of lowercase English letters 'a' through 'j' inclusive.
# Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord,
# or false otherwise.
#
# Example 1:
#
# Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
# Output: true
# Explanation:
# The numerical value of firstWord is "acb" -> "021" -> 21.
# The numerical value of secondWord is "cba" -> "210" -> 210.
# The numerical value of targetWord is "cdb" -> "231" -> 231.
# We return true because 21 + 210 == 231.
#
# Example 2:
#
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
# Output: false
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aab" -> "001" -> 1.
# We return false because 0 + 0 != 1.
#
# Example 3:
#
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
# Output: true
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aaaa" -> "0000" -> 0.
# We return true because 0 + 0 == 0.
#
#
# Constraints:
#
# 1 <= firstWord.length, secondWord.length, targetWord.length <= 8
# firstWord,secondWord,and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.
#
#


#
# [1880] Check if Word Equals Summation of Two Words
# Difficulty: Easy
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words
#
# The letter value of a letter is its position in the alphabet starting from 0 (i.e.'a' -> 0,'b' -> 1,
# etc.).
#
# which is then converted into an integer.
#
# For example,if s = "acb",we concatenate each letter's letter value,resulting in "021".
# we get 21.
#
# You are given three strings firstWord,secondWord,and targetWord,
#
# or false otherwise.
#
# Example 1:
#
# Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
# Output: true
# Explanation:
# The numerical value of firstWord is "acb" -> "021" -> 21.
# The numerical value of secondWord is "cba" -> "210" -> 210.
# The numerical value of targetWord is "cdb" -> "231" -> 231.
# We return true because 21 + 210 == 231.
#
# Example 2:
#
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
# Output: false
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aab" -> "001" -> 1.
# We return false because 0 + 0 != 1.
#
# Example 3:
#
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
# Output: true
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aaaa" -> "0000" -> 0.
# We return true because 0 + 0 == 0.
#
#
# Constraints:
#
# 1 <= firstWord.length, secondWord.length, targetWord.length <= 8
# firstWord,secondWord,and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.
#
#


# class Solution:
#     def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
#         alp_map = dict(tuple(zip("abcdefghij", range(10))))

#         def word2num(word):
#             ans = ""
#             for i in word:
#                 ans += str(alp_map[i])
#             return ans

#         first_num, second_num = word2num(firstWord), word2num(secondWord)
#         target_num = word2num(targetWord)

#         drop_0 = lambda x: int(x[:-1].lstrip("0") + x[-1])
#         first_num = drop_0(first_num)
#         second_num = drop_0(second_num)
#         target_num = drop_0(target_num)

#         return (first_num + second_num) == target_num


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        get_num = lambda word: int("".join([str(ord(alp) - ord("a")) for alp in word]))
        return get_num(firstWord) + get_num(secondWord) == get_num(targetWord)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1880.py")])
