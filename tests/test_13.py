#!/usr/bin/env python

import pytest

"""
Test 13. Roman to Integer
"""


@pytest.fixture(scope="session")
def init_variables_13():
    from src.leetcode_13_roman_to_integer import Solution

    solution = Solution()

    def _init_variables_13():
        return solution

    yield _init_variables_13


class TestClass13:
    def test_solution_0(self, init_variables_13):
        assert init_variables_13().romanToInt("III") == 3

    def test_solution_1(self, init_variables_13):
        assert init_variables_13().romanToInt("IV") == 4

    def test_solution_2(self, init_variables_13):
        assert init_variables_13().romanToInt("IX") == 9

    def test_solution_3(self, init_variables_13):
        assert init_variables_13().romanToInt("LVIII") == 58

    def test_solution_4(self, init_variables_13):
        assert init_variables_13().romanToInt("MCMXCIV") == 1994
