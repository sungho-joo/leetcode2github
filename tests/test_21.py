#!/usr/bin/env python

import pytest

"""
Test 21. Merge Two Sorted Lists
"""


@pytest.fixture(scope="session")
def init_variables_21():
    from src.leetcode_21_merge_two_sorted_lists import Solution

    solution = Solution()

    def _init_variables_21():
        return solution

    yield _init_variables_21


class TestClass21:
    def test_solution_0(self, init_variables_21):
        assert init_variables_21().mergeTwoLists([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]

    def test_solution_1(self, init_variables_21):
        assert init_variables_21().mergeTwoLists([], []) == []

    def test_solution_2(self, init_variables_21):
        assert init_variables_21().mergeTwoLists([], [0]) == [0]
