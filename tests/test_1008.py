#!/usr/bin/env python

import pytest

"""
Test 1008. Construct Binary Search Tree from Preorder Traversal
"""


@pytest.fixture(scope="session")
def init_variables_1008():
    from src.leetcode_1008_construct_binary_search_tree_from_preorder_traversal import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1008():
        return solution

    yield _init_variables_1008


class TestClass1008:
    def test_solution_0(self, init_variables_1008):
        assert init_variables_1008().bstFromPreorder([8, 5, 1, 7, 10, 12]) == [8, 5, 10, 1, 7, None, 12]

    def test_solution_1(self, init_variables_1008):
        assert init_variables_1008().bstFromPreorder([1, 3]) == [1, None, 3]
