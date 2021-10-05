#!/usr/bin/env python

import pytest

"""
Test 572. Subtree of Another Tree
"""


@pytest.fixture(scope="session")
def init_variables_572():
    from src.leetcode_572_subtree_of_another_tree import Solution

    solution = Solution()

    def _init_variables_572():
        return solution

    yield _init_variables_572


class TestClass572:
    def test_solution_0(self, init_variables_572):
        assert init_variables_572().isSubtree([3, 4, 5, 1, 2], [4, 1, 2])

    def test_solution_1(self, init_variables_572):
        assert not init_variables_572().isSubtree([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2])
