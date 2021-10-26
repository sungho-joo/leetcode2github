#!/usr/bin/env python

import pytest

"""
Test 371. Sum of Two Integers
"""


@pytest.fixture(scope="session")
def init_variables_371():
    from src.leetcode_371_sum_of_two_integers import Solution

    solution = Solution()

    def _init_variables_371():
        return solution

    yield _init_variables_371


class TestClass371:
    def test_solution_0(self, init_variables_371):
        assert init_variables_371().getSum(1, 2) == 3

    def test_solution_1(self, init_variables_371):
        assert init_variables_371().getSum(2, 3) == 5
