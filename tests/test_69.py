#!/usr/bin/env python

import pytest

"""
Test 69. Sqrt(x)
"""


@pytest.fixture(scope="session")
def init_variables_69():
    from src.leetcode_69_sqrtx import Solution

    solution = Solution()

    def _init_variables_69():
        return solution

    yield _init_variables_69


class TestClass69:
    def test_solution_0(self, init_variables_69):
        assert init_variables_69().mySqrt(4) == 2

    def test_solution_1(self, init_variables_69):
        assert init_variables_69().mySqrt(8) == 2
