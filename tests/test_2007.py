#!/usr/bin/env python

import pytest

"""
Test 2007. Find Original Array From Doubled Array
"""


@pytest.fixture(scope="session")
def init_variables_2007():
    from src.leetcode_2007_find_original_array_from_doubled_array import Solution

    solution = Solution()

    def _init_variables_2007():
        return solution

    yield _init_variables_2007


class TestClass2007:
    def test_solution_0(self, init_variables_2007):
        assert init_variables_2007().findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4]

    def test_solution_1(self, init_variables_2007):
        assert init_variables_2007().findOriginalArray([6, 3, 0, 1]) == []

    def test_solution_2(self, init_variables_2007):
        assert init_variables_2007().findOriginalArray([1]) == []
