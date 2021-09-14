#!/usr/bin/env python

import pytest

"""
Test 1984. Minimum Difference Between Highest and Lowest of K Scores
"""


@pytest.fixture(scope="session")
def init_variables_1984():
    from src.leetcode_1984_minimum_difference_between_highest_and_lowest_of_k_scores import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1984():
        return solution

    yield _init_variables_1984


class TestClass1984:
    def test_solution_0(self, init_variables_1984):
        assert init_variables_1984().minimumDifference([90], 1) == 0

    def test_solution_1(self, init_variables_1984):
        assert init_variables_1984().minimumDifference([9, 4, 1, 7], 2) == 2
