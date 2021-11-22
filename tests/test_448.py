#!/usr/bin/env python

import pytest

"""
Test 448. Find All Numbers Disappeared in an Array
"""


@pytest.fixture(scope="session")
def init_variables_448():
    from src.leetcode_448_find_all_numbers_disappeared_in_an_array import Solution

    solution = Solution()

    def _init_variables_448():
        return solution

    yield _init_variables_448


class TestClass448:
    def test_solution_0(self, init_variables_448):
        assert init_variables_448().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

    def test_solution_1(self, init_variables_448):
        assert init_variables_448().findDisappearedNumbers([1, 1]) == [2]
