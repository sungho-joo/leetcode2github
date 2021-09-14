#!/usr/bin/env python

import pytest

"""
Test 7. Reverse Integer
"""


@pytest.fixture(scope="session")
def init_variables_7():
    from src.leetcode_7_reverse_integer import Solution

    solution = Solution()

    def _init_variables_7():
        return solution

    yield _init_variables_7


class TestClass7:
    def test_solution_0(self, init_variables_7):
        assert init_variables_7().reverse(123) == 321

    def test_solution_1(self, init_variables_7):
        assert init_variables_7().reverse(-123) == -321

    def test_solution_2(self, init_variables_7):
        assert init_variables_7().reverse(120) == 21

    def test_solution_3(self, init_variables_7):
        assert init_variables_7().reverse(0) == 0
