# @l2g 1957 python3
# [1957] Delete Characters to Make Fancy String
# Difficulty: Easy
# https://leetcode.com/problems/delete-characters-to-make-fancy-string
#
# A fancy string is a string where no three consecutive characters are equal.
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# Return the final string after the deletion. It can be shown that the answer will always be unique.
#
# Example 1:
#
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
#
# Example 2:
#
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
#
# Example 3:
#
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists only of lowercase English letters.
#
#


# TC : O(n), SC : O(n)


class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n < 3:
            return s

        ans = [s[0], s[1]]
        for i in range(2, n):
            if ans[-1] == ans[-2] == s[i]:
                continue
            ans.append(s[i])
        return "".join(ans)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1957.py")])
