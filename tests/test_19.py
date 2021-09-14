#!/usr/bin/env python

import pytest

"""
Test 19. Remove Nth Node From End of List
"""


@pytest.fixture(scope="session")
def init_variables_19():
    from src.leetcode_19_remove_nth_node_from_end_of_list import Solution

    solution = Solution()

    def _init_variables_19():
        return solution

    yield _init_variables_19


class TestClass19:
    def test_solution_0(self, init_variables_19):
        assert init_variables_19().removeNthFromEnd([1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]

    def test_solution_1(self, init_variables_19):
        assert init_variables_19().removeNthFromEnd([1], 1) == []

    def test_solution_2(self, init_variables_19):
        assert init_variables_19().removeNthFromEnd([1, 2], 1) == [1]
