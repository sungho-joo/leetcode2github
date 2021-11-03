#!/usr/bin/env python

import pytest

"""
Test 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
"""


@pytest.fixture(scope="session")
def init_variables_2058():
    from src.leetcode_2058_find_the_minimum_and_maximum_number_of_nodes_between_critical_points import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2058():
        return solution

    yield _init_variables_2058


class TestClass2058:
    def test_solution_0(self, init_variables_2058):
        assert init_variables_2058().nodesBetweenCriticalPoints([3, 1]) == [-1, -1]

    def test_solution_1(self, init_variables_2058):
        assert init_variables_2058().nodesBetweenCriticalPoints([5, 3, 1, 2, 5, 1, 2]) == [1, 3]

    def test_solution_2(self, init_variables_2058):
        assert init_variables_2058().nodesBetweenCriticalPoints([1, 3, 2, 2, 3, 2, 2, 2, 7]) == [3, 3]

    def test_solution_3(self, init_variables_2058):
        assert init_variables_2058().nodesBetweenCriticalPoints([2, 3, 3, 2]) == [-1, -1]
