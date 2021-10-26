#!/usr/bin/env python

import pytest

"""
Test 154. Find Minimum in Rotated Sorted Array II
"""


@pytest.fixture(scope="session")
def init_variables_154():
    from src.leetcode_154_find_minimum_in_rotated_sorted_array_ii import Solution

    solution = Solution()

    def _init_variables_154():
        return solution

    yield _init_variables_154


class TestClass154:
    def test_solution_0(self, init_variables_154):
        assert init_variables_154().findMin([1, 3, 5]) == 1

    def test_solution_1(self, init_variables_154):
        assert init_variables_154().findMin([2, 2, 2, 0, 1]) == 0
