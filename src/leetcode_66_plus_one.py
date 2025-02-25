# @l2g 66 python3
# [66] Plus One
# Difficulty: Easy
# https://leetcode.com/problems/plus-one
#
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
#
# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
# Example 2:
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#
# Example 3:
#
# Input: digits = [0]
# Output: [1]
# Explanation: The array represents the integer 0.
# Incrementing by one gives 0 + 1 = 1.
# Thus, the result should be [1].
#
# Example 4:
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#
#
# Constraints:
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
#
#

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = True
        pos = len(digits) - 1
        while 0 <= pos and plus_one:
            if digits[pos] != 9:
                digits[pos] += 1
                plus_one = False
            else:
                digits[pos] = 0
                plus_one = True
                pos -= 1
        return digits if digits[0] != 0 else [1] + digits

        # return list(map(int, str(int("".join(map(str, digits))) + 1)))


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_66.py")])
