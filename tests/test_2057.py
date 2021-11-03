#!/usr/bin/env python

import pytest

"""
Test 2057. Smallest Index With Equal Value
"""


@pytest.fixture(scope="session")
def init_variables_2057():
    from src.leetcode_2057_smallest_index_with_equal_value import Solution

    solution = Solution()

    def _init_variables_2057():
        return solution

    yield _init_variables_2057


class TestClass2057:
    def test_solution_0(self, init_variables_2057):
        assert init_variables_2057().smallestEqual([0, 1, 2]) == 0

    def test_solution_1(self, init_variables_2057):
        assert init_variables_2057().smallestEqual([4, 3, 2, 1]) == 2

    def test_solution_2(self, init_variables_2057):
        assert init_variables_2057().smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1

    def test_solution_3(self, init_variables_2057):
        assert init_variables_2057().smallestEqual([2, 1, 3, 5, 2]) == 1
