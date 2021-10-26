#!/usr/bin/env python

import pytest

"""
Test 993. Cousins in Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_993():
    from src.leetcode_993_cousins_in_binary_tree import Solution

    solution = Solution()

    def _init_variables_993():
        return solution

    yield _init_variables_993


class TestClass993:
    def test_solution_0(self, init_variables_993):
        assert not init_variables_993().isCousins([1, 2, 3, 4], 4, 3)

    def test_solution_1(self, init_variables_993):
        assert init_variables_993().isCousins([1, 2, 3, None, 4, None, 5], 5, 4)

    def test_solution_2(self, init_variables_993):
        assert not init_variables_993().isCousins([1, 2, 3, None, 4], 2, 3)
