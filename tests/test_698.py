#!/usr/bin/env python

import pytest

"""
Test 698. Partition to K Equal Sum Subsets
"""


@pytest.fixture(scope="session")
def init_variables_698():
    from src.leetcode_698_partition_to_k_equal_sum_subsets import Solution

    solution = Solution()

    def _init_variables_698():
        return solution

    yield _init_variables_698


class TestClass698:
    def test_solution_0(self, init_variables_698):
        assert init_variables_698().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)

    def test_solution_1(self, init_variables_698):
        assert not init_variables_698().canPartitionKSubsets([1, 2, 3, 4], 3)
