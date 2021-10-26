#!/usr/bin/env python

import pytest

"""
Test 34. Find First and Last Position of Element in Sorted Array
"""


@pytest.fixture(scope="session")
def init_variables_34():
    from src.leetcode_34_find_first_and_last_position_of_element_in_sorted_array import (
        Solution,
    )

    solution = Solution()

    def _init_variables_34():
        return solution

    yield _init_variables_34


class TestClass34:
    def test_solution_0(self, init_variables_34):
        assert init_variables_34().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    def test_solution_1(self, init_variables_34):
        assert init_variables_34().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    def test_solution_2(self, init_variables_34):
        assert init_variables_34().searchRange([], 0) == [-1, -1]
