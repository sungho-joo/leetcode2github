#!/usr/bin/env python

import pytest

"""
Test 994. Rotting Oranges
"""


@pytest.fixture(scope="session")
def init_variables_994():
    from src.leetcode_994_rotting_oranges import Solution

    solution = Solution()

    def _init_variables_994():
        return solution

    yield _init_variables_994


class TestClass994:
    def test_solution_0(self, init_variables_994):
        assert init_variables_994().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4

    def test_solution_1(self, init_variables_994):
        assert init_variables_994().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1

    def test_solution_2(self, init_variables_994):
        assert init_variables_994().orangesRotting([[0, 2]]) == 0
