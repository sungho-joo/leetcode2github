#!/usr/bin/env python

import pytest

"""
Test 2034. Stock Price Fluctuation 
"""


@pytest.fixture(scope="session")
def init_variables_2034():
    from src.leetcode_2034_stock_price_fluctuation import Solution

    solution = Solution()

    def _init_variables_2034():
        return solution

    yield _init_variables_2034


class TestClass2034:
    def test_solution_0(self, init_variables_2034):
        assert (
            init_variables_2034().update(
                [
                    "StockPrice",
                    "update",
                    "update",
                    "current",
                    "maximum",
                    "update",
                    "maximum",
                    "update",
                    "minimum",
                ],
                [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []],
            )
            == [None, None, None, 5, 10, None, 5, None, 2]
        )
