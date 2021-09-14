#!/usr/bin/env python

import pytest

"""
Test 915. Partition Array into Disjoint Intervals
"""


@pytest.fixture(scope="session")
def init_variables_915():
    from src.leetcode_915_partition_array_into_disjoint_intervals import Solution

    solution = Solution()

    def _init_variables_915():
        return solution

    yield _init_variables_915


class TestClass915:
    def test_solution_0(self, init_variables_915):
        assert init_variables_915().partitionDisjoint([5, 0, 3, 8, 6]) == 3

    def test_solution_1(self, init_variables_915):
        assert init_variables_915().partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4


#!/usr/bin/env python

import pytest

"""
Test 915. Partition Array into Disjoint Intervals
"""


@pytest.fixture(scope="session")
def init_variables_915():
    from src.leetcode_915_partition_array_into_disjoint_intervals import Solution

    solution = Solution()

    def _init_variables_915():
        return solution

    yield _init_variables_915


class TestClass915:
    def test_solution_0(self, init_variables_915):
        assert init_variables_915().partitionDisjoint([5, 0, 3, 8, 6]) == 3

    def test_solution_1(self, init_variables_915):
        assert init_variables_915().partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4
