# @l2g 1974 python3
# [1974] Minimum Time to Type Word Using Special Typewriter
# Difficulty: Easy
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter
#
# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
# A character can only be typed if the pointer is pointing to that character.
# The pointer is initially pointing to the character 'a'.
#
# Each second, you may perform one of the following operations:
#
# Move the pointer one character counterclockwise or clockwise.
# Type the character the pointer is currently on.
#
# Given a string word, return the minimum number of seconds to type out the characters in word.
#
# Example 1:
#
# Input: word = "abc"
# Output: 5
# Explanation:
# The characters are printed as follows:
# - Type the character 'a' in 1 second since the pointer is initially on 'a'.
# - Move the pointer clockwise to 'b' in 1 second.
# - Type the character 'b' in 1 second.
# - Move the pointer clockwise to 'c' in 1 second.
# - Type the character 'c' in 1 second.
#
# Example 2:
#
# Input: word = "bza"
# Output: 7
# Explanation:
# The characters are printed as follows:
# - Move the pointer clockwise to 'b' in 1 second.
# - Type the character 'b' in 1 second.
# - Move the pointer counterclockwise to 'z' in 2 seconds.
# - Type the character 'z' in 1 second.
# - Move the pointer clockwise to 'a' in 1 second.
# - Type the character 'a' in 1 second.
#
# Example 3:
#
# Input: word = "zjpc"
# Output: 34
# Explanation:
# The characters are printed as follows:
# - Move the pointer counterclockwise to 'z' in 1 second.
# - Type the character 'z' in 1 second.
# - Move the pointer clockwise to 'j' in 10 seconds.
# - Type the character 'j' in 1 second.
# - Move the pointer clockwise to 'p' in 6 seconds.
# - Type the character 'p' in 1 second.
# - Move the pointer counterclockwise to 'c' in 13 seconds.
# - Type the character 'c' in 1 second.
#
#
# Constraints:
#
# 1 <= word.length <= 100
# word consists of lowercase English letters.
#
#


class Solution:
    def minTimeToType(self, word: str) -> int:
        prev_pos = 0
        ans = 0
        for alp in word:
            cur_num = ord(alp) - ord("a")
            clockwise_dist = abs(cur_num - prev_pos)
            anticlock_dist = 26 - clockwise_dist
            move = min(clockwise_dist, anticlock_dist)
            ans += move + 1
            prev_pos = cur_num
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1974.py")])
