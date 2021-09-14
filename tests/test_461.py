#!/usr/bin/env python

import pytest

"""
Test 461. Hamming Distance
"""


@pytest.fixture(scope="session")
def init_variables_461():
    from src.leetcode_461_hamming_distance import Solution

    solution = Solution()

    def _init_variables_461():
        return solution

    yield _init_variables_461


class TestClass461:
    def test_solution_0(self, init_variables_461):
        assert init_variables_461().hammingDistance(1, 4) == 2

    def test_solution_1(self, init_variables_461):
        assert init_variables_461().hammingDistance(3, 1) == 1
