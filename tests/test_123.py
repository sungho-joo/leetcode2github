#!/usr/bin/env python

import pytest

"""
Test 123. Best Time to Buy and Sell Stock III
"""


@pytest.fixture(scope="session")
def init_variables_123():
    from src.leetcode_123_best_time_to_buy_and_sell_stock_iii import Solution

    solution = Solution()

    def _init_variables_123():
        return solution

    yield _init_variables_123


class TestClass123:
    def test_solution_0(self, init_variables_123):
        assert init_variables_123().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6

    def test_solution_1(self, init_variables_123):
        assert init_variables_123().maxProfit([1, 2, 3, 4, 5]) == 4

    def test_solution_2(self, init_variables_123):
        assert init_variables_123().maxProfit([7, 6, 4, 3, 1]) == 0

    def test_solution_3(self, init_variables_123):
        assert init_variables_123().maxProfit([1]) == 0
