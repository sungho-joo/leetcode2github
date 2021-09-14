#!/usr/bin/env python

import pytest

"""
Test 446. Arithmetic Slices II - Subsequence
"""


@pytest.fixture(scope="session")
def init_variables_446():
    from src.leetcode_446_arithmetic_slices_ii_subsequence import Solution

    solution = Solution()

    def _init_variables_446():
        return solution

    yield _init_variables_446


class TestClass446:
    def test_solution_0(self, init_variables_446):
        assert init_variables_446().numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7

    def test_solution_1(self, init_variables_446):
        assert init_variables_446().numberOfArithmeticSlices([7, 7, 7, 7, 7]) == 16
