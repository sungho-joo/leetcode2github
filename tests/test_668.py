#!/usr/bin/env python

import pytest

"""
Test 668. Kth Smallest Number in Multiplication Table
"""


@pytest.fixture(scope="session")
def init_variables_668():
    from src.leetcode_668_kth_smallest_number_in_multiplication_table import Solution

    solution = Solution()

    def _init_variables_668():
        return solution

    yield _init_variables_668


class TestClass668:
    def test_solution_0(self, init_variables_668):
        assert init_variables_668().findKthNumber(3, 3, 5) == 3

    def test_solution_1(self, init_variables_668):
        assert init_variables_668().findKthNumber(2, 3, 6) == 6
