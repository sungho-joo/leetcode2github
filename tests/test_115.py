#!/usr/bin/env python

import pytest

"""
Test 115. Distinct Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_115():
    from src.leetcode_115_distinct_subsequences import Solution

    solution = Solution()

    def _init_variables_115():
        return solution

    yield _init_variables_115


class TestClass115:
    def test_solution_0(self, init_variables_115):
        assert init_variables_115().numDistinct("rabbbit", "rabbit") == 3

    def test_solution_1(self, init_variables_115):
        assert init_variables_115().numDistinct("babgbag", "bag") == 5
