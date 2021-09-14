# @l2g 1825 python3
# [1825] Finding MK Average
# Difficulty: Hard
# https://leetcode.com/problems/finding-mk-average
#
# You are given two integers,m and k,and a stream of integers.
# You are tasked to implement a data structure that calculates the MKAverage for the stream.
# The MKAverage can be calculated using these steps:
#
# If the number of the elements in the stream is less than m you should consider the MKAverage to be -1.
# Otherwise,copy the last m elements of the stream to a separate container.
# Remove the smallest k elements and the largest k elements from the container.
# Calculate the average value for the rest of the elements rounded down to the nearest integer.
#
# Implement the MKAverage class:
#
# MKAverage(int m,
# int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
# void addElement(int num) Inserts a new element num into the stream.
# int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.
#
#
# Example 1:
#
# Input
# ["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage",
# "addElement","addElement","addElement","calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# Output
# [null, null, null, -1, null, 3, null, null, null, 5]
#
# Explanation
# MKAverage obj = new MKAverage(3, 1);
# obj.addElement(3);        // current elements are [3]
# obj.addElement(1);        // current elements are [3,1]
# obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
# obj.addElement(10);       // current elements are [3,1,10]
# obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
#                           // After removing smallest and largest 1 element the container will be [3].
#                           // The average of [3] equals 3/1 = 3, return 3
# obj.addElement(5);        // current elements are [3,1,10,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5,5]
# obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
#                           // After removing smallest and largest 1 element the container will be [5].
#                           // The average of [5] equals 5/1 = 5, return 5
#
#
# Constraints:
#
# 3 <= m <= 10^5
# 1 <= k*2 < m
# 1 <= num <= 10^5
# At most 10^5 calls will be made to addElement and calculateMKAverage.
#
#

from sortedcontainers import SortedList


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.container: deque = deque()
        self.sl = SortedList()
        self.total = 0
        self.small_k, self.big_k = 0, 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.container.append(num)
        ind = self.sl.bisect_left(num)
        # when num is within smallest k numbers
        if ind < self.k:
            self.small_k += num
            if len(self.sl) >= self.k:
                self.small_k -= self.sl[self.k - 1]

        # when num is within biggest k numbers
        if ind >= len(self.sl) + 1 - self.k:
            self.big_k += num
            if len(self.sl) >= self.k:
                self.big_k -= self.sl[-self.k]

        self.sl.add(num)
        if len(self.container) > self.m:
            pop_num = self.container.popleft()
            self.total -= pop_num
            pop_index = self.sl.index(pop_num)
            if pop_index < self.k:
                self.small_k -= pop_num
                self.small_k += self.sl[self.k]
            if pop_index >= len(self.sl) - self.k:
                self.big_k -= pop_num
                self.big_k += self.sl[-self.k - 1]
            self.sl.remove(pop_num)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1

        return (self.total - self.small_k - self.big_k) // (self.m - 2 * self.k)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1825.py")])
