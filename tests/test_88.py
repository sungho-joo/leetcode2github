#!/usr/bin/env python

import pytest

"""
Test 88. Merge Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_88():
    from src.leetcode_88_merge_sorted_array import Solution

    solution = Solution()

    def _init_variables_88():
        return solution

    yield _init_variables_88


class TestClass88:
    def test_solution_0(self, init_variables_88):
        assert init_variables_88().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]

    def test_solution_1(self, init_variables_88):
        assert init_variables_88().merge([1], 1, [], 0) == [1]

    def test_solution_2(self, init_variables_88):
        assert init_variables_88().merge([0], 0, [1], 1) == [1]
