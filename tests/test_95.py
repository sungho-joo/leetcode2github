#!/usr/bin/env python

import pytest

"""
Test 95. Unique Binary Search Trees II
"""


@pytest.fixture(scope="session")
def init_variables_95():
    from src.leetcode_95_unique_binary_search_trees_ii import Solution

    solution = Solution()

    def _init_variables_95():
        return solution

    yield _init_variables_95


class TestClass95:
    def test_solution_0(self, init_variables_95):
        assert init_variables_95().generateTrees(3) == [
            [1, None, 2, None, 3],
            [1, None, 3, 2],
            [2, 1, 3],
            [3, 1, None, None, 2],
            [3, 2, None, 1],
        ]

    def test_solution_1(self, init_variables_95):
        assert init_variables_95().generateTrees(1) == [[1]]
