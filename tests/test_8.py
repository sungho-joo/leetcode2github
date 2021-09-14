#!/usr/bin/env python

import pytest

"""
Test 8. String to Integer (atoi)
"""


@pytest.fixture(scope="session")
def init_variables_8():
    from src.leetcode_8_string_to_integer_atoi import Solution

    solution = Solution()

    def _init_variables_8():
        return solution

    yield _init_variables_8


class TestClass8:
    def test_solution_0(self, init_variables_8):
        assert init_variables_8().myAtoi("42") == 42

    def test_solution_1(self, init_variables_8):
        assert init_variables_8().myAtoi("   -42") == -42

    def test_solution_2(self, init_variables_8):
        assert init_variables_8().myAtoi("4193 with words") == 4193

    def test_solution_3(self, init_variables_8):
        assert init_variables_8().myAtoi("words and 987") == 0

    def test_solution_4(self, init_variables_8):
        assert init_variables_8().myAtoi("-91283472332") == -2147483648
