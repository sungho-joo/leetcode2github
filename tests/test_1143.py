#!/usr/bin/env python

import pytest

"""
Test 1143. Longest Common Subsequence
"""


@pytest.fixture(scope="session")
def init_variables_1143():
    from src.leetcode_1143_longest_common_subsequence import Solution

    solution = Solution()

    def _init_variables_1143():
        return solution

    yield _init_variables_1143


class TestClass1143:
    def test_solution_0(self, init_variables_1143):
        assert init_variables_1143().longestCommonSubsequence("abcde", "ace") == 3

    def test_solution_1(self, init_variables_1143):
        assert init_variables_1143().longestCommonSubsequence("abc", "abc") == 3

    def test_solution_2(self, init_variables_1143):
        assert init_variables_1143().longestCommonSubsequence("abc", "def") == 0
