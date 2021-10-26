# @l2g 2034 python3
# [2034] Stock Price Fluctuation
# Difficulty: Medium
# https://leetcode.com/problems/stock-price-fluctuation
#
# You are given a stream of records about a particular stock.
# Each record contains a timestamp and the corresponding price of the stock at that timestamp.
# Unfortunately due to the volatile nature of the stock market,the records do not come in order.
# Even worse,some records may be incorrect.
# Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.
# Design an algorithm that:
#
# Updates the price of the stock at a particular timestamp,
# correcting the price from any previous records at the timestamp.
# Finds the latest price of the stock based on the current records.
# The latest price is the price at the latest timestamp recorded.
# Finds the maximum price the stock has been based on the current records.
# Finds the minimum price the stock has been based on the current records.
#
# Implement the StockPrice class:
#
# StockPrice() Initializes the object with no price records.
# void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
# int current() Returns the latest price of the stock.
# int maximum() Returns the maximum price of the stock.
# int minimum() Returns the minimum price of the stock.
#
#
# Example 1:
#
# Input
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# Output
# [null, null, null, 5, 10, null, 5, null, 2]
#
# Explanation
# StockPrice stockPrice = new StockPrice();
# stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
# stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
# stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
# stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
# stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
#                           // Timestamps are [1,2] with corresponding prices [3,5].
# stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
# stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
# stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
#
#
# Constraints:
#
# 1 <= timestamp, price <= 10^9
# At most 10^5 calls will be made in total to update, current, maximum, and minimum.
# current, maximum, and minimum will be called only after update has been called at least once.
#
#

import heapq


class StockPrice:
    def __init__(self):
        self.stock_dict = defaultdict(int)
        self.cur_value = []
        self.max_value = []
        self.min_value = []

    def update(self, timestamp: int, price: int) -> None:
        self.stock_dict[timestamp] = price
        if not self.cur_value or self.cur_value[0] <= timestamp:
            self.cur_value = [timestamp, price]
        heapq.heappush(self.max_value, [-price, timestamp])
        heapq.heappush(self.min_value, [price, timestamp])

    def current(self) -> int:
        return self.cur_value[1]

    def maximum(self) -> int:
        while self.stock_dict[self.max_value[0][1]] != -self.max_value[0][0]:
            heapq.heappop(self.max_value)
        return -self.max_value[0][0]

    def minimum(self) -> int:
        while self.stock_dict[self.min_value[0][1]] != self.min_value[0][0]:
            heapq.heappop(self.min_value)
        return self.min_value[0][0]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2034.py")])
