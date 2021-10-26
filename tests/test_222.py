#!/usr/bin/env python

import pytest

"""
Test 222. Count Complete Tree Nodes
"""


@pytest.fixture(scope="session")
def init_variables_222():
    from src.leetcode_222_count_complete_tree_nodes import Solution

    solution = Solution()

    def _init_variables_222():
        return solution

    yield _init_variables_222


class TestClass222:
    def test_solution_0(self, init_variables_222):
        assert init_variables_222().countNodes([1, 2, 3, 4, 5, 6]) == 6

    def test_solution_1(self, init_variables_222):
        assert init_variables_222().countNodes([]) == 0

    def test_solution_2(self, init_variables_222):
        assert init_variables_222().countNodes([1]) == 1
