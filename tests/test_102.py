#!/usr/bin/env python

import pytest

"""
Test 102. Binary Tree Level Order Traversal
"""


@pytest.fixture(scope="session")
def init_variables_102():
    from src.leetcode_102_binary_tree_level_order_traversal import Solution

    solution = Solution()

    def _init_variables_102():
        return solution

    yield _init_variables_102


class TestClass102:
    def test_solution_0(self, init_variables_102):
        assert init_variables_102().levelOrder([3, 9, 20, None, None, 15, 7]) == [[3], [9, 20], [15, 7]]

    def test_solution_1(self, init_variables_102):
        assert init_variables_102().levelOrder([1]) == [[1]]

    def test_solution_2(self, init_variables_102):
        assert init_variables_102().levelOrder([]) == []
