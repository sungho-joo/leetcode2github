#!/usr/bin/env python

import pytest

"""
Test 814. Binary Tree Pruning
"""


@pytest.fixture(scope="session")
def init_variables_814():
    from src.leetcode_814_binary_tree_pruning import Solution

    solution = Solution()

    def _init_variables_814():
        return solution

    yield _init_variables_814


class TestClass814:
    def test_solution_0(self, init_variables_814):
        assert init_variables_814().pruneTree([1, None, 0, 0, 1]) == [1, None, 0, None, 1]

    def test_solution_1(self, init_variables_814):
        assert init_variables_814().pruneTree([1, 0, 1, 0, 0, 0, 1]) == [1, None, 1, None, 1]

    def test_solution_2(self, init_variables_814):
        assert init_variables_814().pruneTree([1, 1, 0, 1, 1, 0, 1, 0]) == [1, 1, 0, 1, 1, None, 1]


#!/usr/bin/env python

import pytest

"""
Test 814. Binary Tree Pruning
"""


@pytest.fixture(scope="session")
def init_variables_814():
    from src.leetcode_814_binary_tree_pruning import Solution

    solution = Solution()

    def _init_variables_814():
        return solution

    yield _init_variables_814


class TestClass814:
    def test_solution_0(self, init_variables_814):
        assert init_variables_814().pruneTree([1, None, 0, 0, 1]) == [1, None, 0, None, 1]

    def test_solution_1(self, init_variables_814):
        assert init_variables_814().pruneTree([1, 0, 1, 0, 0, 0, 1]) == [1, None, 1, None, 1]

    def test_solution_2(self, init_variables_814):
        assert init_variables_814().pruneTree([1, 1, 0, 1, 1, 0, 1, 0]) == [1, 1, 0, 1, 1, None, 1]
