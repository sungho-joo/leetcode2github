#!/usr/bin/env python

import pytest

"""
Test 1995. Count Special Quadruplets
"""


@pytest.fixture(scope="session")
def init_variables_1995():
    from src.leetcode_1995_count_special_quadruplets import Solution

    solution = Solution()

    def _init_variables_1995():
        return solution

    yield _init_variables_1995


class TestClass1995:
    def test_solution_0(self, init_variables_1995):
        assert init_variables_1995().countQuadruplets([1, 2, 3, 6]) == 1

    def test_solution_1(self, init_variables_1995):
        assert init_variables_1995().countQuadruplets([3, 3, 6, 4, 5]) == 0

    def test_solution_2(self, init_variables_1995):
        assert init_variables_1995().countQuadruplets([1, 1, 1, 3, 5]) == 4
