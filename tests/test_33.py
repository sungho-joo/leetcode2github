#!/usr/bin/env python

import pytest

"""
Test 33. Search in Rotated Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_33():
    from src.leetcode_33_search_in_rotated_sorted_array import Solution

    solution = Solution()

    def _init_variables_33():
        return solution

    yield _init_variables_33


class TestClass33:
    def test_solution_0(self, init_variables_33):
        assert init_variables_33().search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_solution_1(self, init_variables_33):
        assert init_variables_33().search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_solution_2(self, init_variables_33):
        assert init_variables_33().search([1], 0) == -1
