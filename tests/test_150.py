#!/usr/bin/env python

import pytest

"""
Test 150. Evaluate Reverse Polish Notation
"""


@pytest.fixture(scope="session")
def init_variables_150():
    from src.leetcode_150_evaluate_reverse_polish_notation import Solution

    solution = Solution()

    def _init_variables_150():
        return solution

    yield _init_variables_150


class TestClass150:
    def test_solution_0(self, init_variables_150):
        assert init_variables_150().evalRPN(["2", "1", "+", "3", "*"]) == 9

    def test_solution_1(self, init_variables_150):
        assert init_variables_150().evalRPN(["4", "13", "5", "/", "+"]) == 6

    def test_solution_2(self, init_variables_150):
        assert (
            init_variables_150().evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            )
            == 22
        )
