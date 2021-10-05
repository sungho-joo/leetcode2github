#!/usr/bin/env python

import pytest

"""
Test 22. Generate Parentheses
"""


@pytest.fixture(scope="session")
def init_variables_22():
    from src.leetcode_22_generate_parentheses import Solution

    solution = Solution()

    def _init_variables_22():
        return solution

    yield _init_variables_22


class TestClass22:
    def test_solution_0(self, init_variables_22):
        assert init_variables_22().generateParenthesis(3) == [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()",
        ]

    def test_solution_1(self, init_variables_22):
        assert init_variables_22().generateParenthesis(1) == ["()"]
