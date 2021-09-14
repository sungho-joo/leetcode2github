# @l2g 412 python3
# [412] Fizz Buzz
# Difficulty: Easy
# https://leetcode.com/problems/fizz-buzz
#
# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.
#
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
# 1 <= n <= 10^4
#
#

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1, n + 1)]

        def remove_num(div):
            div_map = {3: "Fizz", 5: "Buzz", 15: "FizzBuzz"}
            num = div - 1
            while num < n:
                ans[num] = div_map[div]
                num += div

        remove_num(3)
        remove_num(5)
        remove_num(15)
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_412.py")])
