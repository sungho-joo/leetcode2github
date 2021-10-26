#!/usr/bin/env python

import pytest

"""
Test 50. Pow(x, n)
"""


@pytest.fixture(scope="session")
def init_variables_50():
    from src.leetcode_50_powx_n import Solution

    solution = Solution()

    def _init_variables_50():
        return solution

    yield _init_variables_50


class TestClass50:
    def test_solution_0(self, init_variables_50):
        assert init_variables_50().myPow(2.00000, 10) == 1024.00000

    def test_solution_1(self, init_variables_50):
        assert init_variables_50().myPow(2.10000, 3) == 9.26100

    def test_solution_2(self, init_variables_50):
        assert init_variables_50().myPow(2.00000, -2) == 0.25000
