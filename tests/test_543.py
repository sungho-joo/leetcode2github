#!/usr/bin/env python

import pytest

"""
Test 543. Diameter of Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_543():
    from src.leetcode_543_diameter_of_binary_tree import Solution

    solution = Solution()

    def _init_variables_543():
        return solution

    yield _init_variables_543


class TestClass543:
    def test_solution_0(self, init_variables_543):
        assert init_variables_543().diameterOfBinaryTree([1, 2, 3, 4, 5]) == 3

    def test_solution_1(self, init_variables_543):
        assert init_variables_543().diameterOfBinaryTree([1, 2]) == 1
