#!/usr/bin/env python

import pytest

"""
Test 75. Sort Colors
"""


@pytest.fixture(scope="session")
def init_variables_75():
    from src.leetcode_75_sort_colors import Solution

    solution = Solution()

    def _init_variables_75():
        return solution

    yield _init_variables_75


class TestClass75:
    def test_solution_0(self, init_variables_75):
        assert init_variables_75().sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    def test_solution_1(self, init_variables_75):
        assert init_variables_75().sortColors([2, 0, 1]) == [0, 1, 2]

    def test_solution_2(self, init_variables_75):
        assert init_variables_75().sortColors([0]) == [0]

    def test_solution_3(self, init_variables_75):
        assert init_variables_75().sortColors([1]) == [1]
