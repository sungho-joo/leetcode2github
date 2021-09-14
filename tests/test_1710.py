#!/usr/bin/env python

import pytest

"""
Test 1710. Maximum Units on a Truck
"""


@pytest.fixture(scope="session")
def init_variables_1710():
    from src.leetcode_1710_maximum_units_on_a_truck import Solution

    solution = Solution()

    def _init_variables_1710():
        return solution

    yield _init_variables_1710


class TestClass1710:
    def test_solution_0(self, init_variables_1710):
        assert init_variables_1710().maximumUnits([[1, 3], [2, 2], [3, 1]], 4) == 8

    def test_solution_1(self, init_variables_1710):
        assert init_variables_1710().maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91
