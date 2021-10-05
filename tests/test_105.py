#!/usr/bin/env python

import pytest

"""
Test 105. Construct Binary Tree from Preorder and Inorder Traversal
"""


@pytest.fixture(scope="session")
def init_variables_105():
    from src.leetcode_105_construct_binary_tree_from_preorder_and_inorder_traversal import (
        Solution,
    )

    solution = Solution()

    def _init_variables_105():
        return solution

    yield _init_variables_105


class TestClass105:
    def test_solution_0(self, init_variables_105):
        assert init_variables_105().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == [
            3,
            9,
            20,
            None,
            None,
            15,
            7,
        ]

    def test_solution_1(self, init_variables_105):
        assert init_variables_105().buildTree([-1], [-1]) == [-1]
