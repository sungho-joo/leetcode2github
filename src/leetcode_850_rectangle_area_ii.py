# @l2g 850 python3
# [850] Rectangle Area II
# Difficulty: Hard
# https://leetcode.com/problems/rectangle-area-ii
#
# We are given a list of (axis-aligned) rectangles.Each rectangle[i] = [xi1,yi1,xi2,yi2] ,where (xi1,
# yi1) are the coordinates of the bottom-left corner,and (xi2,
# yi2) are the coordinates of the top-right corner of the ith rectangle.
# Find the total area covered by all rectangles in the plane.Since the answer may be too large,
# return it modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
#
# Example 2:
#
# Input: rectangles = [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
#
#
# Constraints:
#
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= rectangles[i][j] <= 10^9
# The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
#
#

import bisect
import collections
from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def merge(height_list):
            ans = []
            for start, end in height_list:
                if not ans or start > ans[-1][1]:
                    ans.append([start, end])
                else:
                    ans[-1][1] = max(end, ans[-1][1])
            return sum(e - s for s, e in ans)

        height_dict = collections.defaultdict(list)
        for rect in rectangles:
            height_dict[rect[0]].append((1, rect[1], rect[-1]))
            height_dict[rect[2]].append((-1, rect[1], rect[-1]))

        height_list = list()
        prev_pos = min(height_dict)
        ans = 0
        for x, changes in sorted(height_dict.items()):
            # add ans
            ans += (x - prev_pos) * merge(height_list)

            # update height queue
            for sign, y1, y2 in changes:
                if sign > 0:
                    bisect.insort(height_list, (y1, y2))
                else:
                    height_list.pop(bisect.bisect_left(height_list, (y1, y2)))
            prev_pos = x
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_850.py")])
