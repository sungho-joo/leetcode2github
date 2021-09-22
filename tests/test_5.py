#!/usr/bin/env python

import pytest

"""
Test 5. Longest Palindromic Substring
"""


@pytest.fixture(scope="session")
def init_variables_5():
    from src.leetcode_5_longest_palindromic_substring import Solution

    solution = Solution()

    def _init_variables_5():
        return solution

    yield _init_variables_5


class TestClass5:
    def test_solution_0(self, init_variables_5):
        assert init_variables_5().longestPalindrome("babad") == "bab"

    def test_solution_1(self, init_variables_5):
        assert init_variables_5().longestPalindrome("cbbd") == "bb"

    def test_solution_2(self, init_variables_5):
        assert init_variables_5().longestPalindrome("a") == "a"

    def test_solution_3(self, init_variables_5):
        assert init_variables_5().longestPalindrome("ac") == "a"
