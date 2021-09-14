#!/usr/bin/env python

import pytest

"""
Test 224. Basic Calculator
"""


@pytest.fixture(scope="session")
def init_variables_224():
    from src.leetcode_224_basic_calculator import Solution

    solution = Solution()

    def _init_variables_224():
        return solution

    yield _init_variables_224


class TestClass224:
    def test_solution_0(self, init_variables_224):
        assert init_variables_224().calculate("1 + 1") == 2

    def test_solution_1(self, init_variables_224):
        assert init_variables_224().calculate(" 2-1 + 2 ") == 3

    def test_solution_2(self, init_variables_224):
        assert init_variables_224().calculate("(1+(4+5+2)-3)+(6+8)") == 23
