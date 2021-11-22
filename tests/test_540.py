#!/usr/bin/env python

import pytest

"""
Test 540. Single Element in a Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_540():
    from src.leetcode_540_single_element_in_a_sorted_array import Solution

    solution = Solution()

    def _init_variables_540():
        return solution

    yield _init_variables_540


class TestClass540:
    def test_solution_0(self, init_variables_540):
        assert init_variables_540().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2

    def test_solution_1(self, init_variables_540):
        assert init_variables_540().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
