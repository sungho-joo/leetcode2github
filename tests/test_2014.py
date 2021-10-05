#!/usr/bin/env python

import pytest

"""
Test 2014. Longest Subsequence Repeated k Times
"""


@pytest.fixture(scope="session")
def init_variables_2014():
    from src.leetcode_2014_longest_subsequence_repeated_k_times import Solution

    solution = Solution()

    def _init_variables_2014():
        return solution

    yield _init_variables_2014


class TestClass2014:
    def test_solution_0(self, init_variables_2014):
        assert init_variables_2014().longestSubsequenceRepeatedK("letsleetcode", 2) == "let"

    def test_solution_1(self, init_variables_2014):
        assert init_variables_2014().longestSubsequenceRepeatedK("bb", 2) == "b"

    def test_solution_2(self, init_variables_2014):
        assert init_variables_2014().longestSubsequenceRepeatedK("ab", 2) == ""

    def test_solution_3(self, init_variables_2014):
        assert init_variables_2014().longestSubsequenceRepeatedK("bbabbabbbbabaababab", 3) == "bbbb"
