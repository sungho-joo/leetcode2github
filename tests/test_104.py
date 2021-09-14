#!/usr/bin/env python

import pytest

"""
Test 104. Maximum Depth of Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_104():
    from src.leetcode_104_maximum_depth_of_binary_tree import Solution

    solution = Solution()

    def _init_variables_104():
        return solution

    yield _init_variables_104


class TestClass104:
    def test_solution_0(self, init_variables_104):
        assert init_variables_104().maxDepth([3, 9, 20, None, None, 15, 7]) == 3

    def test_solution_1(self, init_variables_104):
        assert init_variables_104().maxDepth([1, None, 2]) == 2

    def test_solution_2(self, init_variables_104):
        assert init_variables_104().maxDepth([]) == 0

    def test_solution_3(self, init_variables_104):
        assert init_variables_104().maxDepth([0]) == 1
