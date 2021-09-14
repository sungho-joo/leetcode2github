#!/usr/bin/env python

import pytest

"""
Test 2002. Maximum Product of the Length of Two Palindromic Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_2002():
    from src.leetcode_2002_maximum_product_of_the_length_of_two_palindromic_subsequences import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2002():
        return solution

    yield _init_variables_2002


class TestClass2002:
    def test_solution_0(self, init_variables_2002):
        assert init_variables_2002().maxProduct("leetcodecom") == 9

    def test_solution_1(self, init_variables_2002):
        assert init_variables_2002().maxProduct("bb") == 1

    def test_solution_2(self, init_variables_2002):
        assert init_variables_2002().maxProduct("accbcaxxcxx") == 25
