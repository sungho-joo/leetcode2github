# @l2g 1792 python3
# [1792] Maximum Average Pass Ratio
# Difficulty: Medium
# https://leetcode.com/problems/maximum-average-pass-ratio
#
# There is a school that has classes of students and each class will be having a final exam.
# You are given a 2D integer array classes,where classes[i] = [passi,totali].
# You know beforehand that in the ith class,there are totali total students,
# but only passi number of students will pass the exam.
# You are also given an integer extraStudents.
# There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to.
# You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class.
# The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
# Return the maximum possible average pass ratio after assigning the extraStudents students.
# Answers within 10-5 of the actual answer will be accepted.
#
# Example 1:
#
# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class.
# The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
#
# Example 2:
#
# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485
#
#
# Constraints:
#
# 1 <= classes.length <= 10^5
# classes[i].length == 2
# 1 <= passi <= totali <= 10^5
# 1 <= extraStudents <= 10^5
#
#

import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def get_increment(pass_i, total_i):
            return float((total_i - pass_i) / (total_i * (total_i + 1)))

        # class_info = []
        ratio_sum = 0.0
        increment_heap: List[List] = []
        for ind, (p, t) in enumerate(classes):
            ratio = float(p / t)
            ratio_sum += ratio
            increment = get_increment(p, t)
            heapq.heappush(increment_heap, [-increment, p, t, ratio, increment])
            # class_info.append([ind, p, t, ratio, increment])

        for _ in range(extraStudents):
            max_class = heapq.heappop(increment_heap)
            ratio_sum += max_class[-1]
            max_class[1] += 1
            max_class[2] += 1
            max_class[3] = float(max_class[1] / max_class[2])
            max_class[4] = get_increment(max_class[1], max_class[2])
            max_class[0] = -max_class[4]

            heapq.heappush(increment_heap, max_class)

        return ratio_sum / len(classes)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1792.py")])
