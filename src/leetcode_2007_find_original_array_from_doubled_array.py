# @l2g 2007 python3
# [2007] Find Original Array From Doubled Array
# Difficulty: Medium
# https://leetcode.com/problems/find-original-array-from-doubled-array
#
# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original,
# and then randomly shuffling the resulting array.
# Given an array changed,return original if changed is a doubled array.
# If changed is not a doubled array,return an empty array.
# The elements in original may be returned in any order.
#
# Example 1:
#
# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
#
# Example 2:
#
# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
#
# Example 3:
#
# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.
#
#
# Constraints:
#
# 1 <= changed.length <= 10^5
# 0 <= changed[i] <= 10^5
#
#

from typing import Counter, List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        sorted_arr = sorted(changed)
        ans = []
        if len(changed) % 2 != 0:
            return []
        if len(count) == 1 and count[0] > 1:
            return [0] * (count[0] // 2)
        for i in range(len(sorted_arr)):
            if count[sorted_arr[i]] > 0 and count[sorted_arr[i] * 2] > 0:
                count[sorted_arr[i]] -= 1
                count[sorted_arr[i] * 2] -= 1
                ans.append(sorted_arr[i])
        # print(count)
        return ans if all(val == 0 for val in count.values()) else []


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2007.py")])
