#!/usr/bin/env python

import pytest

"""
Test 1998. GCD Sort of an Array
"""


@pytest.fixture(scope="session")
def init_variables_1998():
    from src.leetcode_1998_gcd_sort_of_an_array import Solution

    solution = Solution()

    def _init_variables_1998():
        return solution

    yield _init_variables_1998


class TestClass1998:
    def test_solution_0(self, init_variables_1998):
        assert init_variables_1998().gcdSort([7, 21, 3])

    def test_solution_1(self, init_variables_1998):
        assert not init_variables_1998().gcdSort([5, 2, 6, 2])

    def test_solution_2(self, init_variables_1998):
        assert init_variables_1998().gcdSort([10, 5, 9, 3, 15])
