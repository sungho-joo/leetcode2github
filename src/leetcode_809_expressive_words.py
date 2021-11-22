# @l2g 809 python3
# [809] Expressive Words
# Difficulty: Medium
# https://leetcode.com/problems/expressive-words
#
# Sometimes people repeat letters to represent extra feeling. For example:
#
# "hello" -> "heeellooo"
# "hi" -> "hiiii"
#
# In these strings like "heeellooo",we have groups of adjacent letters that are all the same: "h",
# "eee","ll","ooo".
# You are given a string s and an array of query strings words.
# A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c,
# and add some number of characters c to the group so that the size of the group is three or more.
#
# For example,starting with "hello",we could do an extension on the group "o" to get "hellooo",
# but we cannot get "helloo" since the group "oo" has a size less than three.Also,
# we could do another extension like "ll" -> "lllll" to get "helllllooo".If s = "helllllooo",
# then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
#
# Return the number of query strings that are stretchy.
#
# Example 1:
#
# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
#
# Example 2:
#
# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3
#
#
# Constraints:
#
# 1 <= s.length, words.length <= 100
# 1 <= words[i].length <= 100
# s and words[i] consist of lowercase letters.
#
#

from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_word_groups(word):
            word_group = []
            cnt = 1
            for i in range(1, len(word)):
                if word[i] != word[i - 1]:
                    word_group.append([word[i - 1], cnt])
                    cnt = 1
                else:
                    cnt += 1
            word_group.append([word[-1], cnt])
            return word_group

        s_group = get_word_groups(s)

        ans = 0
        for cur_word in words:
            cur_word_group = get_word_groups(cur_word)
            # Length check
            if len(s_group) != len(cur_word_group):
                continue

            is_stretchy = True
            # Check length and alphabet of group
            for subgroup_1, subgroup_2 in zip(s_group, cur_word_group):
                alp1, len_1 = subgroup_1
                alp2, len_2 = subgroup_2
                if alp1 != alp2:
                    is_stretchy = False
                    break

                condition_1 = len_2 < len_1 and 3 <= len_1
                condition_2 = len_2 == len_1
                if not (condition_1 or condition_2):
                    is_stretchy = False
                    break

            ans += int(is_stretchy)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_809.py")])
