#!/usr/bin/env python

import pytest

"""
Test 103. Binary Tree Zigzag Level Order Traversal
"""


@pytest.fixture(scope="session")
def init_variables_103():
    from src.leetcode_103_binary_tree_zigzag_level_order_traversal import Solution

    solution = Solution()

    def _init_variables_103():
        return solution

    yield _init_variables_103


class TestClass103:
    def test_solution_0(self, init_variables_103):
        assert init_variables_103().zigzagLevelOrder([3, 9, 20, None, None, 15, 7]) == [
            [3],
            [20, 9],
            [15, 7],
        ]

    def test_solution_1(self, init_variables_103):
        assert init_variables_103().zigzagLevelOrder([1]) == [[1]]

    def test_solution_2(self, init_variables_103):
        assert init_variables_103().zigzagLevelOrder([]) == []
