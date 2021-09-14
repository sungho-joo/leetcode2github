#!/usr/bin/env python

import pytest

"""
Test 834. Sum of Distances in Tree
"""


@pytest.fixture(scope="session")
def init_variables_834():
    from src.leetcode_834_sum_of_distances_in_tree import Solution

    solution = Solution()

    def _init_variables_834():
        return solution

    yield _init_variables_834


class TestClass834:
    def test_solution_0(self, init_variables_834):
        assert init_variables_834().sumOfDistancesInTree(
            6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
        ) == [8, 12, 6, 10, 10, 10]

    def test_solution_1(self, init_variables_834):
        assert init_variables_834().sumOfDistancesInTree(1, []) == [0]

    def test_solution_2(self, init_variables_834):
        assert init_variables_834().sumOfDistancesInTree(2, [[1, 0]]) == [1, 1]
