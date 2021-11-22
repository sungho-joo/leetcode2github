#!/usr/bin/env python

import pytest

"""
Test 450. Delete Node in a BST
"""


@pytest.fixture(scope="session")
def init_variables_450():
    from src.leetcode_450_delete_node_in_a_bst import Solution

    solution = Solution()

    def _init_variables_450():
        return solution

    yield _init_variables_450


class TestClass450:
    def test_solution_0(self, init_variables_450):
        assert init_variables_450().deleteNode([5, 3, 6, 2, 4, None, 7], 3) == [
            5,
            4,
            6,
            2,
            None,
            None,
            7,
        ]

    def test_solution_1(self, init_variables_450):
        assert init_variables_450().deleteNode([5, 3, 6, 2, 4, None, 7], 0) == [5, 3, 6, 2, 4, None, 7]

    def test_solution_2(self, init_variables_450):
        assert init_variables_450().deleteNode([], 0) == []
