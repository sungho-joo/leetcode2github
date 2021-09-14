#!/usr/bin/env python

import pytest

"""
Test 141. Linked List Cycle
"""


@pytest.fixture(scope="session")
def init_variables_141():
    from src.leetcode_141_linked_list_cycle import Solution

    solution = Solution()

    def _init_variables_141():
        return solution

    yield _init_variables_141


class TestClass141:
    def test_solution_0(self, init_variables_141):
        assert init_variables_141().hasCycle([3, 2, 0, -4], 1)

    def test_solution_1(self, init_variables_141):
        assert init_variables_141().hasCycle([1, 2], 0)

    def test_solution_2(self, init_variables_141):
        assert not init_variables_141().hasCycle([1], -1)
