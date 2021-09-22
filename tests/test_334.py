#!/usr/bin/env python

import pytest

"""
Test 334. Increasing Triplet Subsequence
"""


@pytest.fixture(scope="session")
def init_variables_334():
    from src.leetcode_334_increasing_triplet_subsequence import Solution

    solution = Solution()

    def _init_variables_334():
        return solution

    yield _init_variables_334


class TestClass334:
    def test_solution_0(self, init_variables_334):
        assert init_variables_334().increasingTriplet([1, 2, 3, 4, 5])

    def test_solution_1(self, init_variables_334):
        assert not init_variables_334().increasingTriplet([5, 4, 3, 2, 1])

    def test_solution_2(self, init_variables_334):
        assert init_variables_334().increasingTriplet([2, 1, 5, 0, 4, 6])
