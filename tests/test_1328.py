#!/usr/bin/env python

import pytest

"""
Test 1328. Break a Palindrome
"""


@pytest.fixture(scope="session")
def init_variables_1328():
    from src.leetcode_1328_break_a_palindrome import Solution

    solution = Solution()

    def _init_variables_1328():
        return solution

    yield _init_variables_1328


class TestClass1328:
    def test_solution_0(self, init_variables_1328):
        assert init_variables_1328().breakPalindrome("abccba") == "aaccba"

    def test_solution_1(self, init_variables_1328):
        assert init_variables_1328().breakPalindrome("a") == ""

    def test_solution_2(self, init_variables_1328):
        assert init_variables_1328().breakPalindrome("aa") == "ab"

    def test_solution_3(self, init_variables_1328):
        assert init_variables_1328().breakPalindrome("aba") == "abb"
