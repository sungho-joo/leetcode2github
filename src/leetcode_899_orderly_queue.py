# @l2g 899 python3
# [899] Orderly Queue
# Difficulty: Hard
# https://leetcode.com/problems/orderly-queue
#
# You are given a string s and an integer k.
# You can choose one of the first k letters of s and append it at the end of the string..
# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.
#
# Example 1:
#
# Input: s = "cba", k = 1
# Output: "acb"
# Explanation:
# In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
# In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
#
# Example 2:
#
# Input: s = "baaca", k = 3
# Output: "aaabc"
# Explanation:
# In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
# In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
#
#
# Constraints:
#
# 1 <= k <= s.length <= 1000
# s consist of lowercase English letters.
#
#


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        s_list = list(s)
        sorted_s = sorted(s_list)
        if k == 1:
            return "".join(min([s_list[i:] + s_list[:i] for i in range(n)]))

        return "".join(sorted_s)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_899.py")])
