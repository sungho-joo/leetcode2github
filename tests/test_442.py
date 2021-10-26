#!/usr/bin/env python

import pytest

"""
Test 442. Find All Duplicates in an Array
"""


@pytest.fixture(scope="session")
def init_variables_442():
    from src.leetcode_442_find_all_duplicates_in_an_array import Solution

    solution = Solution()

    def _init_variables_442():
        return solution

    yield _init_variables_442


class TestClass442:
    def test_solution_0(self, init_variables_442):
        assert init_variables_442().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]

    def test_solution_1(self, init_variables_442):
        assert init_variables_442().findDuplicates([1, 1, 2]) == [1]

    def test_solution_2(self, init_variables_442):
        assert init_variables_442().findDuplicates([1]) == []
