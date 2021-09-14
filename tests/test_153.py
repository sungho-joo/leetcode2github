#!/usr/bin/env python

import pytest

"""
Test 153. Find Minimum in Rotated Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_153():
    from src.leetcode_153_find_minimum_in_rotated_sorted_array import Solution

    solution = Solution()

    def _init_variables_153():
        return solution

    yield _init_variables_153


class TestClass153:
    def test_solution_0(self, init_variables_153):
        assert init_variables_153().findMin([3, 4, 5, 1, 2]) == 1

    def test_solution_1(self, init_variables_153):
        assert init_variables_153().findMin([4, 5, 6, 7, 0, 1, 2]) == 0

    def test_solution_2(self, init_variables_153):
        assert init_variables_153().findMin([11, 13, 15, 17]) == 11
