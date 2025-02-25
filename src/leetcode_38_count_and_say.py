# @l2g 38 python3
# [38] Count and Say
# Difficulty: Medium
# https://leetcode.com/problems/count-and-say
#
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
#
# To determine how you "say" a digit string,
# split it into the minimal number of groups so that each group is a contiguous section all of the same character.
# Then for each group,say the number of characters,then say the character.
# To convert the saying into a digit string,
# replace the counts with a number and concatenate every saying.
# For example, the saying and conversion for digit string "3322251":
#
# Given a positive integer n, return the nth term of the count-and-say sequence.
#
# Example 1:
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#
# Example 2:
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
#
#
# Constraints:
#
# 1 <= n <= 30
#
#


class Solution:
    def countAndSay(self, n: int) -> str:
        self.dp = [None] * 30
        self.dp[0] = "1"

        def get_next_string(arr):
            new_string = []
            prev_num = arr[0]
            for num in arr:
                if not new_string or num != prev_num:
                    new_string.extend([0, num])
                    prev_num = num
                new_string[-2] += 1
            return new_string

        string = "1"
        for i in range(n):
            if self.dp[i]:
                string = self.dp[i]
                continue
            new_string = get_next_string(string)
            string = "".join(str(num) for num in new_string)
            self.dp[i] = string
        return string


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_38.py")])
