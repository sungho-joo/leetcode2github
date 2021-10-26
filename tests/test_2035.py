#!/usr/bin/env python

import pytest

"""
Test 2035. Partition Array Into Two Arrays to Minimize Sum Difference
"""


@pytest.fixture(scope="session")
def init_variables_2035():
    from src.leetcode_2035_partition_array_into_two_arrays_to_minimize_sum_difference import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2035():
        return solution

    yield _init_variables_2035


class TestClass2035:
    def test_solution_0(self, init_variables_2035):
        assert init_variables_2035().minimumDifference([3, 9, 7, 3]) == 2

    def test_solution_1(self, init_variables_2035):
        assert init_variables_2035().minimumDifference([-36, 36]) == 72

    def test_solution_2(self, init_variables_2035):
        assert init_variables_2035().minimumDifference([2, -1, 0, 4, -2, -9]) == 0
