#!/usr/bin/env python

import pytest

"""
Test 1818. Minimum Absolute Sum Difference
"""


@pytest.fixture(scope="session")
def init_variables_1818():
    from src.leetcode_1818_minimum_absolute_sum_difference import Solution

    solution = Solution()

    def _init_variables_1818():
        return solution

    yield _init_variables_1818


class TestClass1818:
    def test_solution_0(self, init_variables_1818):
        assert init_variables_1818().minAbsoluteSumDiff([1, 7, 5], [2, 3, 5]) == 3

    def test_solution_1(self, init_variables_1818):
        assert init_variables_1818().minAbsoluteSumDiff([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]) == 0

    def test_solution_2(self, init_variables_1818):
        assert init_variables_1818().minAbsoluteSumDiff([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4]) == 20
