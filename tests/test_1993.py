#!/usr/bin/env python

import pytest

"""
Test 1993. Operations on Tree
"""


@pytest.fixture(scope="session")
def init_variables_1993():
    from src.leetcode_1993_operations_on_tree import LockingTree

    solution = LockingTree([-1, 0, 0, 1, 1, 2, 2])

    def _init_variables_1993():
        return solution

    yield _init_variables_1993


class TestClass1993:
    def test_solution_0(self, init_variables_1993):
        assert init_variables_1993().lock(2, 2) == True
        assert init_variables_1993().unlock(2, 3) == False
        assert init_variables_1993().unlock(2, 2) == True
        assert init_variables_1993().lock(4, 5) == True
        assert init_variables_1993().upgrade(0, 1) == True
        assert init_variables_1993().lock(0, 1) == False
