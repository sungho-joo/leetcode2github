# @l2g 1235 python3
# [1235] Maximum Profit in Job Scheduling
# Difficulty: Hard
# https://leetcode.com/problems/maximum-profit-in-job-scheduling
#
# We have n jobs,where every job is scheduled to be done from startTime[i] to endTime[i],
# obtaining a profit of profit[i].
# You're given the startTime,endTime and profit arrays,
# return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
#
# Example 1:
#
#
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
# Example 2:
#
#
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
#
# Example 3:
#
#
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
#
# Constraints:
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4
#
#

import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        last_time = max(startTime)

        sorted_list = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        time_list = sorted(startTime)
        time_list.append(float("inf"))

        @lru_cache(None)
        def dp(pos):
            if time_list[pos] > last_time:
                return 0
            st, et, pft = sorted_list[pos]
            next_pos = bisect.bisect_left(time_list, et)
            ans = max(dp(pos + 1), pft + dp(next_pos))
            return ans

        return dp(0)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1235.py")])
