#!/usr/bin/env python

import pytest

"""
Test 101. Symmetric Tree
"""


@pytest.fixture(scope="session")
def init_variables_101():
    from src.leetcode_101_symmetric_tree import Solution

    solution = Solution()

    def _init_variables_101():
        return solution

    yield _init_variables_101


class TestClass101:
    def test_solution_0(self, init_variables_101):
        assert init_variables_101().isSymmetric([1, 2, 2, 3, 4, 4, 3])

    def test_solution_1(self, init_variables_101):
        assert not init_variables_101().isSymmetric([1, 2, 2, None, 3, None, 3])
