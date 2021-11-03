#!/usr/bin/env python

import pytest

"""
Test 130. Surrounded Regions
"""


@pytest.fixture(scope="session")
def init_variables_130():
    from src.leetcode_130_surrounded_regions import Solution

    solution = Solution()

    def _init_variables_130():
        return solution

    yield _init_variables_130


class TestClass130:
    def test_solution_0(self, init_variables_130):
        assert init_variables_130().solve(
            [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        ) == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    def test_solution_1(self, init_variables_130):
        assert init_variables_130().solve([["X"]]) == [["X"]]
