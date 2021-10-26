#!/usr/bin/env python

import pytest

"""
Test 172. Factorial Trailing Zeroes
"""


@pytest.fixture(scope="session")
def init_variables_172():
    from src.leetcode_172_factorial_trailing_zeroes import Solution

    solution = Solution()

    def _init_variables_172():
        return solution

    yield _init_variables_172


class TestClass172:
    def test_solution_0(self, init_variables_172):
        assert init_variables_172().trailingZeroes(3) == 0

    def test_solution_1(self, init_variables_172):
        assert init_variables_172().trailingZeroes(5) == 1

    def test_solution_2(self, init_variables_172):
        assert init_variables_172().trailingZeroes(0) == 0
