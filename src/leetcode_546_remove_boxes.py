# @l2g 546 python3
# [546] Remove Boxes
# Difficulty: Hard
# https://leetcode.com/problems/remove-boxes
#
# You are given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (i.e.,composed of k boxes,
# k >= 1),remove them and get k * k points.
# Return the maximum points you can get.
#
# Example 1:
#
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
#
# Example 2:
#
# Input: boxes = [1,1,1]
# Output: 9
#
# Example 3:
#
# Input: boxes = [1]
# Output: 1
#
#
# Constraints:
#
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
#
#

from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            ans = (k + 1) ** 2 + dp(l + 1, r, 0)

            for i in range(l + 1, r + 1):
                if boxes[l] == boxes[i]:
                    ans = max(ans, dp(l + 1, i - 1, 0) + dp(i, r, k + 1))
            return ans

        return dp(0, len(boxes) - 1, 0)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_546.py")])
