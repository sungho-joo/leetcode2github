#!/usr/bin/env python

import pytest

"""
Test 1991. Find the Middle Index in Array
"""


@pytest.fixture(scope="session")
def init_variables_1991():
    from src.leetcode_1991_find_the_middle_index_in_array import Solution

    solution = Solution()

    def _init_variables_1991():
        return solution

    yield _init_variables_1991


class TestClass1991:
    def test_solution_0(self, init_variables_1991):
        assert init_variables_1991().findMiddleIndex([2, 3, -1, 8, 4]) == 3

    def test_solution_1(self, init_variables_1991):
        assert init_variables_1991().findMiddleIndex([1, -1, 4]) == 2

    def test_solution_2(self, init_variables_1991):
        assert init_variables_1991().findMiddleIndex([2, 5]) == -1

    def test_solution_3(self, init_variables_1991):
        assert init_variables_1991().findMiddleIndex([1]) == 0
