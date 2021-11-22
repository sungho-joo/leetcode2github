# @l2g 2054 python3
# [2054] Two Best Non-Overlapping Events
# Difficulty: Medium
# https://leetcode.com/problems/two-best-non-overlapping-events
#
# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei,endTimei,valuei].
# The ith event starts at startTimei and ends at endTimei,and if you attend this event,
# you will receive a value of valuei.
# You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.
# Return this maximum sum.
# Note that the start time and end time is inclusive: that is,
# you cannot attend two events where one of them starts and the other ends at the same time.
# More specifically,if you attend an event with end time t,
# the next event must start at or after t + 1.
#
# Example 1:
#
#
# Input: events = [[1,3,2],[4,5,2],[2,4,3]]
# Output: 4
# Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
#
# Example 2:
#
#
# Input: events = [[1,3,2],[4,5,2],[1,5,5]]
# Output: 5
# Explanation: Choose event 2 for a sum of 5.
#
# Example 3:
#
#
# Input: events = [[1,5,3],[1,5,1],[6,6,5]]
# Output: 8
# Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
#
# Constraints:
#
# 2 <= events.length <= 10^5
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 10^9
# 1 <= valuei <= 10^6
#
#

import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        start_map = defaultdict(int)
        end_map = defaultdict(int)
        time_map = set()
        ans = -float("inf")
        for s, e, v in events:
            start_map[s] = max(start_map[s], v)
            end_map[e] = max(end_map[e], v)
            time_map.add(s)
            time_map.add(e)
            ans = max(ans, v)

        start_times = sorted(start_map.keys())
        end_times = sorted(end_map.keys())
        time_line = sorted(time_map)

        right_path = [0] * len(start_times)
        max_right = -float("inf")
        for i in range(len(start_times) - 1, -1, -1):
            max_right = max(max_right, start_map[start_times[i]])
            right_path[i] = max_right

        left_path = [0] * len(end_times)
        max_left = -float("inf")
        for i in range(len(end_times)):
            max_left = max(max_left, end_map[end_times[i]])
            left_path[i] = max_left

        start_times.append(float("inf"))
        for i, time in enumerate(end_times):
            left = left_path[i]
            next_time = bisect.bisect_left(start_times, time + 1)
            if next_time == len(start_times) - 1:
                break
            right = right_path[next_time]
            ans = max(ans, left + right)

        return ans


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2054.py")])
