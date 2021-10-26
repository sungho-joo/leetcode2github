#!/usr/bin/env python

import pytest

"""
Test 2025. Maximum Number of Ways to Partition an Array
"""


@pytest.fixture(scope="session")
def init_variables_2025():
    from src.leetcode_2025_maximum_number_of_ways_to_partition_an_array import Solution

    solution = Solution()

    def _init_variables_2025():
        return solution

    yield _init_variables_2025


class TestClass2025:
    def test_solution_0(self, init_variables_2025):
        assert init_variables_2025().waysToPartition([2, -1, 2], 3) == 1

    def test_solution_1(self, init_variables_2025):
        assert init_variables_2025().waysToPartition([0, 0, 0], 1) == 2

    def test_solution_2(self, init_variables_2025):
        assert (
            init_variables_2025().waysToPartition(
                [22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], -33
            )
            == 4
        )
