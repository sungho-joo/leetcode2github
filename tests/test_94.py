#!/usr/bin/env python

import pytest

"""
Test 94. Binary Tree Inorder Traversal
"""


@pytest.fixture(scope="session")
def init_variables_94():
    from src.leetcode_94_binary_tree_inorder_traversal import Solution

    solution = Solution()

    def _init_variables_94():
        return solution

    yield _init_variables_94


class TestClass94:
    def test_solution_0(self, init_variables_94):
        assert init_variables_94().inorderTraversal([1, None, 2, 3]) == [1, 3, 2]

    def test_solution_1(self, init_variables_94):
        assert init_variables_94().inorderTraversal([]) == []

    def test_solution_2(self, init_variables_94):
        assert init_variables_94().inorderTraversal([1]) == [1]

    def test_solution_3(self, init_variables_94):
        assert init_variables_94().inorderTraversal([1, 2]) == [2, 1]

    def test_solution_4(self, init_variables_94):
        assert init_variables_94().inorderTraversal([1, None, 2]) == [1, 2]
