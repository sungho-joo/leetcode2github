# @l2g 1189 python3
# [1189] Maximum Number of Balloons
# Difficulty: Easy
# https://leetcode.com/problems/maximum-number-of-balloons
#
# Given a string text,
# you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once.
# Return the maximum number of instances that can be formed.
#
# Example 1:
#
#
# Input: text = "nlaebolko"
# Output: 1
#
# Example 2:
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
#
# Example 3:
#
# Input: text = "leetcode"
# Output: 0
#
#
# Constraints:
#
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.
#
#

from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        count["l"] //= 2
        count["o"] //= 2

        return min(count["b"], count["a"], count["l"], count["o"], count["n"])


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1189.py")])
