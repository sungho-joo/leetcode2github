#!/usr/bin/env python

import pytest

"""
Test 1987. Number of Unique Good Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_1987():
    from src.leetcode_1987_number_of_unique_good_subsequences import Solution

    solution = Solution()

    def _init_variables_1987():
        return solution

    yield _init_variables_1987


class TestClass1987:
    def test_solution_0(self, init_variables_1987):
        assert init_variables_1987().numberOfUniqueGoodSubsequences("001") == 2

    def test_solution_1(self, init_variables_1987):
        assert init_variables_1987().numberOfUniqueGoodSubsequences("11") == 2

    def test_solution_2(self, init_variables_1987):
        assert init_variables_1987().numberOfUniqueGoodSubsequences("101") == 5
