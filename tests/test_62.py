#!/usr/bin/env python

import pytest

"""
Test 62. Unique Paths
"""


@pytest.fixture(scope="session")
def init_variables_62():
    from src.leetcode_62_unique_paths import Solution

    solution = Solution()

    def _init_variables_62():
        return solution

    yield _init_variables_62


class TestClass62:
    def test_solution_0(self, init_variables_62):
        assert init_variables_62().uniquePaths(3, 7) == 28

    def test_solution_1(self, init_variables_62):
        assert init_variables_62().uniquePaths(3, 2) == 3

    def test_solution_2(self, init_variables_62):
        assert init_variables_62().uniquePaths(7, 3) == 28

    def test_solution_3(self, init_variables_62):
        assert init_variables_62().uniquePaths(3, 3) == 6
