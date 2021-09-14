# @l2g 1864 python3
# [1864] Minimum Number of Swaps to Make the Binary String Alternating
# Difficulty: Medium
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating
#
# Given a binary string s,return the minimum number of character swaps to make it alternating,
# or -1 if it is impossible.
# The string is called alternating if no two adjacent characters are equal.For example,
# the strings "010" and "1010" are alternating,while the string "0100" is not.
# Any two characters may be swapped, even if they are not adjacent.
#
# Example 1:
#
# Input: s = "111000"
# Output: 1
# Explanation: Swap positions 1 and 4: "111000" -> "101010"
# The string is now alternating.
#
# Example 2:
#
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating, no swaps are needed.
#
# Example 3:
#
# Input: s = "1110"
# Output: -1
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
#
#

from typing import Counter


class Solution:
    def minSwaps(self, s: str) -> int:
        count = Counter(s)
        diff = abs(count["0"] - count["1"])
        if diff > 1:
            return -1
        elif diff == 1:
            if (count["0"] - count["1"]) == 1:
                target = ["0" + "10" * (len(s) // 2)]
            else:
                target = ["1" + "01" * (len(s) // 2)]

        else:
            target = ["01" * (len(s) // 2), "10" * (len(s) // 2)]
        # print(target)
        ans = 1000
        for target_str in target:
            swap = 0
            for i in range(0, len(s)):
                if s[i] != target_str[i]:
                    swap += 1
            ans = min(ans, swap // 2)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1864.py")])
