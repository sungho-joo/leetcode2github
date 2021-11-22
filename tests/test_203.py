#!/usr/bin/env python

import pytest

"""
Test 203. Remove Linked List Elements
"""


@pytest.fixture(scope="session")
def init_variables_203():
    from src.leetcode_203_remove_linked_list_elements import Solution

    solution = Solution()

    def _init_variables_203():
        return solution

    yield _init_variables_203


class TestClass203:
    def test_solution_0(self, init_variables_203):
        assert init_variables_203().removeElements([1, 2, 6, 3, 4, 5, 6], 6) == [1, 2, 3, 4, 5]

    def test_solution_1(self, init_variables_203):
        assert init_variables_203().removeElements([], 1) == []

    def test_solution_2(self, init_variables_203):
        assert init_variables_203().removeElements([7, 7, 7, 7], 7) == []
