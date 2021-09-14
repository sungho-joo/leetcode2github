# @l2g 56 python3
# [56] Merge Intervals
# Difficulty: Medium
# https://leetcode.com/problems/merge-intervals
#
# Given an array of intervals where intervals[i] = [starti,endi],merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for s, e in sorted(intervals):
            if not ans or ans[-1][1] < s:
                ans.append([s, e])
            else:
                ans[-1][1] = max(e, ans[-1][1])
        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_56.py")])
