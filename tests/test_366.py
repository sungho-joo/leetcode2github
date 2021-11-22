#!/usr/bin/env python

import pytest

"""
Test 366. Find Leaves of Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_366():
    from src.leetcode_366_find_leaves_of_binary_tree import Solution

    solution = Solution()

    def _init_variables_366():
        return solution

    yield _init_variables_366


class TestClass366:
    def test_solution_0(self, init_variables_366):
        assert init_variables_366().findLeaves([1, 2, 3, 4, 5]) == [[4, 5, 3], [2], [1]]

    def test_solution_1(self, init_variables_366):
        assert init_variables_366().findLeaves([1]) == [[1]]
