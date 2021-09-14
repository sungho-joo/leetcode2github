#!/usr/bin/env python

import pytest

"""
Test 268. Missing Number
"""


@pytest.fixture(scope="session")
def init_variables_268():
    from src.leetcode_268_missing_number import Solution

    solution = Solution()

    def _init_variables_268():
        return solution

    yield _init_variables_268


class TestClass268:
    def test_solution_0(self, init_variables_268):
        assert init_variables_268().missingNumber([3, 0, 1]) == 2

    def test_solution_1(self, init_variables_268):
        assert init_variables_268().missingNumber([0, 1]) == 2

    def test_solution_2(self, init_variables_268):
        assert init_variables_268().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

    def test_solution_3(self, init_variables_268):
        assert init_variables_268().missingNumber([0]) == 1
