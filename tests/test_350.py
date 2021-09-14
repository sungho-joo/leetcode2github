#!/usr/bin/env python

import pytest

"""
Test 350. Intersection of Two Arrays II
"""


@pytest.fixture(scope="session")
def init_variables_350():
    from src.leetcode_350_intersection_of_two_arrays_ii import Solution

    solution = Solution()

    def _init_variables_350():
        return solution

    yield _init_variables_350


class TestClass350:
    def test_solution_0(self, init_variables_350):
        assert init_variables_350().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]

    def test_solution_1(self, init_variables_350):
        assert init_variables_350().intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
