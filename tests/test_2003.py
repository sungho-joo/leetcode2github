#!/usr/bin/env python

import pytest

"""
Test 2003. Smallest Missing Genetic Value in Each Subtree
"""


@pytest.fixture(scope="session")
def init_variables_2003():
    from src.leetcode_2003_smallest_missing_genetic_value_in_each_subtree import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2003():
        return solution

    yield _init_variables_2003


class TestClass2003:
    def test_solution_0(self, init_variables_2003):
        assert init_variables_2003().smallestMissingValueSubtree([-1, 0, 0, 2], [1, 2, 3, 4]) == [
            5,
            1,
            1,
            1,
        ]

    def test_solution_1(self, init_variables_2003):
        assert init_variables_2003().smallestMissingValueSubtree(
            [-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3]
        ) == [7, 1, 1, 4, 2, 1]

    def test_solution_2(self, init_variables_2003):
        assert init_variables_2003().smallestMissingValueSubtree(
            [-1, 2, 3, 0, 2, 4, 1], [2, 3, 4, 5, 6, 7, 8]
        ) == [1, 1, 1, 1, 1, 1, 1]
