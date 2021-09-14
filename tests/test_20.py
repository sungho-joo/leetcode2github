#!/usr/bin/env python

import pytest

"""
Test 20. Valid Parentheses
"""


@pytest.fixture(scope="session")
def init_variables_20():
    from src.leetcode_20_valid_parentheses import Solution

    solution = Solution()

    def _init_variables_20():
        return solution

    yield _init_variables_20


class TestClass20:
    def test_solution_0(self, init_variables_20):
        assert init_variables_20().isValid("()")

    def test_solution_1(self, init_variables_20):
        assert init_variables_20().isValid("()[]{}")

    def test_solution_2(self, init_variables_20):
        assert not init_variables_20().isValid("(]")

    def test_solution_3(self, init_variables_20):
        assert not init_variables_20().isValid("([)]")

    def test_solution_4(self, init_variables_20):
        assert init_variables_20().isValid("{[]}")
