#!/usr/bin/env python

import pytest

"""
Test 522. Longest Uncommon Subsequence II
"""


@pytest.fixture(scope="session")
def init_variables_522():
    from src.leetcode_522_longest_uncommon_subsequence_ii import Solution

    solution = Solution()

    def _init_variables_522():
        return solution

    yield _init_variables_522


class TestClass522:
    def test_solution_0(self, init_variables_522):
        assert init_variables_522().findLUSlength(["aba", "cdc", "eae"]) == 3

    def test_solution_1(self, init_variables_522):
        assert init_variables_522().findLUSlength(["aaa", "aaa", "aa"]) == -1
