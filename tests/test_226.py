#!/usr/bin/env python

import pytest

"""
Test 226. Invert Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_226():
    from src.leetcode_226_invert_binary_tree import Solution

    solution = Solution()

    def _init_variables_226():
        return solution

    yield _init_variables_226


class TestClass226:
    def test_solution_0(self, init_variables_226):
        assert init_variables_226().invertTree([4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1]

    def test_solution_1(self, init_variables_226):
        assert init_variables_226().invertTree([2, 1, 3]) == [2, 3, 1]

    def test_solution_2(self, init_variables_226):
        assert init_variables_226().invertTree([]) == []
