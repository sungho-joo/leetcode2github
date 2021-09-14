#!/usr/bin/env python

import pytest

"""
Test 125. Valid Palindrome
"""


@pytest.fixture(scope="session")
def init_variables_125():
    from src.leetcode_125_valid_palindrome import Solution

    solution = Solution()

    def _init_variables_125():
        return solution

    yield _init_variables_125


class TestClass125:
    def test_solution_0(self, init_variables_125):
        assert init_variables_125().isPalindrome("A man, a plan, a canal: Panama")

    def test_solution_1(self, init_variables_125):
        assert not init_variables_125().isPalindrome("race a car")
