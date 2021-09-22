#!/usr/bin/env python

import pytest

"""
Test 2006. Count Number of Pairs With Absolute Difference K
"""


@pytest.fixture(scope="session")
def init_variables_2006():
    from src.leetcode_2006_count_number_of_pairs_with_absolute_difference_k import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2006():
        return solution

    yield _init_variables_2006


class TestClass2006:
    def test_solution_0(self, init_variables_2006):
        assert init_variables_2006().countKDifference([1, 2, 2, 1], 1) == 4

    def test_solution_1(self, init_variables_2006):
        assert init_variables_2006().countKDifference([1, 3], 3) == 0

    def test_solution_2(self, init_variables_2006):
        assert init_variables_2006().countKDifference([3, 2, 1, 5, 4], 2) == 3
