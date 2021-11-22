#!/usr/bin/env python

import pytest

"""
Test 1413. Minimum Value to Get Positive Step by Step Sum
"""


@pytest.fixture(scope="session")
def init_variables_1413():
    from src.leetcode_1413_minimum_value_to_get_positive_step_by_step_sum import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1413():
        return solution

    yield _init_variables_1413


class TestClass1413:
    def test_solution_0(self, init_variables_1413):
        assert init_variables_1413().minStartValue([-3, 2, -3, 4, 2]) == 5

    def test_solution_1(self, init_variables_1413):
        assert init_variables_1413().minStartValue([1, 2]) == 1

    def test_solution_2(self, init_variables_1413):
        assert init_variables_1413().minStartValue([1, -2, -3]) == 5
