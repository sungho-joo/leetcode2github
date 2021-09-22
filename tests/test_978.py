#!/usr/bin/env python

import pytest

"""
Test 978. Longest Turbulent Subarray
"""


@pytest.fixture(scope="session")
def init_variables_978():
    from src.leetcode_978_longest_turbulent_subarray import Solution

    solution = Solution()

    def _init_variables_978():
        return solution

    yield _init_variables_978


class TestClass978:
    def test_solution_0(self, init_variables_978):
        assert init_variables_978().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5

    def test_solution_1(self, init_variables_978):
        assert init_variables_978().maxTurbulenceSize([4, 8, 12, 16]) == 2

    def test_solution_2(self, init_variables_978):
        assert init_variables_978().maxTurbulenceSize([100]) == 1
