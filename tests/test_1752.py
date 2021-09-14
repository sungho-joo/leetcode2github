#!/usr/bin/env python

import pytest

"""
Test 1752. Check if Array Is Sorted and Rotated
"""


@pytest.fixture(scope="session")
def init_variables_1752():
    from src.leetcode_1752_check_if_array_is_sorted_and_rotated import Solution

    solution = Solution()

    def _init_variables_1752():
        return solution

    yield _init_variables_1752


class TestClass1752:
    def test_solution_0(self, init_variables_1752):
        assert init_variables_1752().check([3, 4, 5, 1, 2])

    def test_solution_1(self, init_variables_1752):
        assert not init_variables_1752().check([2, 1, 3, 4])

    def test_solution_2(self, init_variables_1752):
        assert init_variables_1752().check([1, 2, 3])

    def test_solution_3(self, init_variables_1752):
        assert init_variables_1752().check([1, 1, 1])

    def test_solution_4(self, init_variables_1752):
        assert init_variables_1752().check([2, 1])
