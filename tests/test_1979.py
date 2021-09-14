#!/usr/bin/env python

import pytest

"""
Test 1979. Find Greatest Common Divisor of Array
"""


@pytest.fixture(scope="session")
def init_variables_1979():
    from src.leetcode_1979_find_greatest_common_divisor_of_array import Solution

    solution = Solution()

    def _init_variables_1979():
        return solution

    yield _init_variables_1979


class TestClass1979:
    def test_solution_0(self, init_variables_1979):
        assert init_variables_1979().findGCD([2, 5, 6, 9, 10]) == 2

    def test_solution_1(self, init_variables_1979):
        assert init_variables_1979().findGCD([7, 5, 6, 8, 3]) == 1

    def test_solution_2(self, init_variables_1979):
        assert init_variables_1979().findGCD([3, 3]) == 3
