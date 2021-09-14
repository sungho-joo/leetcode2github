#!/usr/bin/env python

import pytest

"""
Test 1727. Largest Submatrix With Rearrangements
"""


@pytest.fixture(scope="session")
def init_variables_1727():
    from src.leetcode_1727_largest_submatrix_with_rearrangements import Solution

    solution = Solution()

    def _init_variables_1727():
        return solution

    yield _init_variables_1727


class TestClass1727:
    def test_solution_0(self, init_variables_1727):
        assert init_variables_1727().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4

    def test_solution_1(self, init_variables_1727):
        assert init_variables_1727().largestSubmatrix([[1, 0, 1, 0, 1]]) == 3

    def test_solution_2(self, init_variables_1727):
        assert init_variables_1727().largestSubmatrix([[1, 1, 0], [1, 0, 1]]) == 2

    def test_solution_3(self, init_variables_1727):
        assert init_variables_1727().largestSubmatrix([[0, 0], [0, 0]]) == 0
