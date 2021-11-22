#!/usr/bin/env python

import pytest

"""
Test 739. Daily Temperatures
"""


@pytest.fixture(scope="session")
def init_variables_739():
    from src.leetcode_739_daily_temperatures import Solution

    solution = Solution()

    def _init_variables_739():
        return solution

    yield _init_variables_739


class TestClass739:
    def test_solution_0(self, init_variables_739):
        assert init_variables_739().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
            1,
            1,
            4,
            2,
            1,
            1,
            0,
            0,
        ]

    def test_solution_1(self, init_variables_739):
        assert init_variables_739().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    def test_solution_2(self, init_variables_739):
        assert init_variables_739().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
