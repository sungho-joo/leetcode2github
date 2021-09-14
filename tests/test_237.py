#!/usr/bin/env python

import pytest

"""
Test 237. Delete Node in a Linked List
"""


@pytest.fixture(scope="session")
def init_variables_237():
    from src.leetcode_237_delete_node_in_a_linked_list import Solution

    solution = Solution()

    def _init_variables_237():
        return solution

    yield _init_variables_237


class TestClass237:
    def test_solution_0(self, init_variables_237):
        assert init_variables_237().deleteNode([4, 5, 1, 9], 5) == [4, 1, 9]

    def test_solution_1(self, init_variables_237):
        assert init_variables_237().deleteNode([4, 5, 1, 9], 1) == [4, 5, 9]

    def test_solution_2(self, init_variables_237):
        assert init_variables_237().deleteNode([1, 2, 3, 4], 3) == [1, 2, 4]

    def test_solution_3(self, init_variables_237):
        assert init_variables_237().deleteNode([0, 1], 0) == [1]

    def test_solution_4(self, init_variables_237):
        assert init_variables_237().deleteNode([-3, 5, -99], -3) == [5, -99]
