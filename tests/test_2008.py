#!/usr/bin/env python

import pytest

"""
Test 2008. Maximum Earnings From Taxi
"""


@pytest.fixture(scope="session")
def init_variables_2008():
    from src.leetcode_2008_maximum_earnings_from_taxi import Solution

    solution = Solution()

    def _init_variables_2008():
        return solution

    yield _init_variables_2008


class TestClass2008:
    def test_solution_0(self, init_variables_2008):
        assert init_variables_2008().maxTaxiEarnings(5, [[2, 5, 4], [1, 5, 1]]) == 7

    def test_solution_1(self, init_variables_2008):
        assert (
            init_variables_2008().maxTaxiEarnings(
                20, [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
            )
            == 20
        )
