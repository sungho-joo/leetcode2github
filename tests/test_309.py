#!/usr/bin/env python

import pytest

"""
Test 309. Best Time to Buy and Sell Stock with Cooldown
"""


@pytest.fixture(scope="session")
def init_variables_309():
    from src.leetcode_309_best_time_to_buy_and_sell_stock_with_cooldown import Solution

    solution = Solution()

    def _init_variables_309():
        return solution

    yield _init_variables_309


class TestClass309:
    def test_solution_0(self, init_variables_309):
        assert init_variables_309().maxProfit([1, 2, 3, 0, 2]) == 3

    def test_solution_1(self, init_variables_309):
        assert init_variables_309().maxProfit([1]) == 0
