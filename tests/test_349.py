#!/usr/bin/env python

import pytest

"""
Test 349. Intersection of Two Arrays
"""


@pytest.fixture(scope="session")
def init_variables_349():
    from src.leetcode_349_intersection_of_two_arrays import Solution

    solution = Solution()

    def _init_variables_349():
        return solution

    yield _init_variables_349


class TestClass349:
    def test_solution_0(self, init_variables_349):
        assert init_variables_349().intersection([1, 2, 2, 1], [2, 2]) == [2]

    def test_solution_1(self, init_variables_349):
        assert init_variables_349().intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
