#!/usr/bin/env python

import pytest

"""
Test 1819. Number of Different Subsequences GCDs
"""


@pytest.fixture(scope="session")
def init_variables_1819():
    from src.leetcode_1819_number_of_different_subsequences_gcds import Solution

    solution = Solution()

    def _init_variables_1819():
        return solution

    yield _init_variables_1819


class TestClass1819:
    def test_solution_0(self, init_variables_1819):
        assert init_variables_1819().countDifferentSubsequenceGCDs([6, 10, 3]) == 5

    def test_solution_1(self, init_variables_1819):
        assert init_variables_1819().countDifferentSubsequenceGCDs([5, 15, 40, 5, 6]) == 7
