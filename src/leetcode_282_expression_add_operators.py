# @l2g 282 python3
# [282] Expression Add Operators
# Difficulty: Hard
# https://leetcode.com/problems/expression-add-operators
#
# Given a string num that contains only digits and an integer target,
# return all possibilities to add the binary operators '+','-',
# or '*' between the digits of num so that the resultant expression evaluates to the target value.
#
# Example 1:
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Example 3:
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:
# Input: num = "00", target = 0
# Output: ["0*0","0+0","0-0"]
# Example 5:
# Input: num = "3456237490", target = 9191
# Output: []
#
#
# Constraints:
#
# 1 <= num.length <= 10
# num consists of only digits.
# -2^31 <= target <= 2^31 - 1
#
#

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        dp = [defaultdict(list) for _ in range(n)]

        def iterate(pos):
            if pos == len(num) - 1:
                dp[pos][int(num[pos])].append((int(num[pos]), num[pos]))
            for i in range(pos + 1, len(num)):
                if i == len(num) - 1 and num[pos] != "0":
                    dp[pos][int(num[pos:])].append((int(num[pos:]), f"{int(num[pos:])}"))

                for key, val in dp[i].items():
                    cur_num = int(num[pos:i])
                    for first_num, expression in val:
                        # add
                        dp[pos][cur_num + key].append((cur_num, f"{cur_num}" + "+" + expression))
                        # subtract
                        dp[pos][cur_num - (2 * first_num) + key].append(
                            (cur_num, f"{cur_num}" + "-" + expression)
                        )
                        # mul
                        dp[pos][cur_num * first_num - first_num + key].append(
                            (cur_num * first_num, f"{cur_num}" + "*" + expression)
                        )
                if num[pos] == "0":
                    break

        for i in range(len(num) - 1, -1, -1):
            iterate(i)

        return [v for k, v in dp[0][target]]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_282.py")])
