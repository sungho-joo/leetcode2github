#!/usr/bin/env python

import pytest

"""
Test 1235. Maximum Profit in Job Scheduling
"""


@pytest.fixture(scope="session")
def init_variables_1235():
    from src.leetcode_1235_maximum_profit_in_job_scheduling import Solution

    solution = Solution()

    def _init_variables_1235():
        return solution

    yield _init_variables_1235


class TestClass1235:
    def test_solution_0(self, init_variables_1235):
        assert init_variables_1235().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120

    def test_solution_1(self, init_variables_1235):
        assert (
            init_variables_1235().jobScheduling(
                [1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]
            )
            == 150
        )

    def test_solution_2(self, init_variables_1235):
        assert init_variables_1235().jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6
