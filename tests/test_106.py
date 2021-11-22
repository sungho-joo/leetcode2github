#!/usr/bin/env python

import pytest

"""
Test 106. Construct Binary Tree from Inorder and Postorder Traversal
"""


@pytest.fixture(scope="session")
def init_variables_106():
    from src.leetcode_106_construct_binary_tree_from_inorder_and_postorder_traversal import (
        Solution,
    )

    solution = Solution()

    def _init_variables_106():
        return solution

    yield _init_variables_106


class TestClass106:
    def test_solution_0(self, init_variables_106):
        assert init_variables_106().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == [
            3,
            9,
            20,
            None,
            None,
            15,
            7,
        ]

    def test_solution_1(self, init_variables_106):
        assert init_variables_106().buildTree([-1], [-1]) == [-1]
