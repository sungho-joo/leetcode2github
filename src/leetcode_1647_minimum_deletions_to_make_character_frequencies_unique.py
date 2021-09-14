# @l2g 1647 python3
# [1647] Minimum Deletions to Make Character Frequencies Unique
# Difficulty: Medium
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique
#
# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string.
# For example,in the string "aab",the frequency of 'a' is 2,while the frequency of 'b' is 1.
#
# Example 1:
#
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
#
# Example 2:
#
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
# Example 3:
#
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e.
# frequency of 0 is ignored).
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
#
#


class Solution:
    def minDeletions(self, s: str) -> int:
        delete_iter = 0
        count_dic = {}

        for cur_alphabet in s:
            if cur_alphabet in count_dic:
                count_dic[cur_alphabet] += 1
            else:
                count_dic[cur_alphabet] = 1

        alphabet_counts = [value for key, value in count_dic.items()]
        alphabet_counts = sorted(alphabet_counts, reverse=True)

        def is_first_unique(alphabet_counts):
            if alphabet_counts[0] == alphabet_counts[1]:
                return False
            else:
                return True

        def find_reduce_pos(alphabet_counts):
            i = 1
            cur_value = alphabet_counts[0]
            while i < len(alphabet_counts):
                if cur_value != alphabet_counts[i]:
                    break
                else:
                    i += 1
            return i - 1

        while len(alphabet_counts) > 1:
            if is_first_unique(alphabet_counts):
                alphabet_counts = alphabet_counts[1:]
            else:
                ind = find_reduce_pos(alphabet_counts)
                alphabet_counts[ind] -= 1
                if alphabet_counts[ind] == 0:
                    alphabet_counts = alphabet_counts[:ind]
                delete_iter += 1
        return delete_iter


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1647.py")])
