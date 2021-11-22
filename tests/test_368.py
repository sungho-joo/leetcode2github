#!/usr/bin/env python

import pytest

"""
Test 368. Largest Divisible Subset
"""


@pytest.fixture(scope="session")
def init_variables_368():
    from src.leetcode_368_largest_divisible_subset import Solution

    solution = Solution()

    def _init_variables_368():
        return solution

    yield _init_variables_368


class TestClass368:
    def test_solution_0(self, init_variables_368):
        assert init_variables_368().largestDivisibleSubset([1, 2, 3]) == [1, 2]

    def test_solution_1(self, init_variables_368):
        assert init_variables_368().largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]
