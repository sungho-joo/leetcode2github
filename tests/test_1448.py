#!/usr/bin/env python

import pytest

"""
Test 1448. Count Good Nodes in Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_1448():
    from src.leetcode_1448_count_good_nodes_in_binary_tree import Solution

    solution = Solution()

    def _init_variables_1448():
        return solution

    yield _init_variables_1448


class TestClass1448:
    def test_solution_0(self, init_variables_1448):
        assert init_variables_1448().goodNodes([3, 1, 4, 3, None, 1, 5]) == 4

    def test_solution_1(self, init_variables_1448):
        assert init_variables_1448().goodNodes([3, 3, None, 4, 2]) == 3

    def test_solution_2(self, init_variables_1448):
        assert init_variables_1448().goodNodes([1]) == 1


#!/usr/bin/env python

import pytest

"""
Test 1448. Count Good Nodes in Binary Tree
"""


@pytest.fixture(scope="session")
def init_variables_1448():
    from src.leetcode_1448_count_good_nodes_in_binary_tree import Solution

    solution = Solution()

    def _init_variables_1448():
        return solution

    yield _init_variables_1448


class TestClass1448:
    def test_solution_0(self, init_variables_1448):
        assert init_variables_1448().goodNodes([3, 1, 4, 3, None, 1, 5]) == 4

    def test_solution_1(self, init_variables_1448):
        assert init_variables_1448().goodNodes([3, 3, None, 4, 2]) == 3

    def test_solution_2(self, init_variables_1448):
        assert init_variables_1448().goodNodes([1]) == 1
