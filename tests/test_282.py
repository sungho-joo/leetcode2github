#!/usr/bin/env python

import pytest

"""
Test 282. Expression Add Operators
"""


@pytest.fixture(scope="session")
def init_variables_282():
    from src.leetcode_282_expression_add_operators import Solution

    solution = Solution()

    def _init_variables_282():
        return solution

    yield _init_variables_282


class TestClass282:
    def test_solution_0(self, init_variables_282):
        assert init_variables_282().addOperators("123", 6) == ["1*2*3", "1+2+3"]

    def test_solution_1(self, init_variables_282):
        assert init_variables_282().addOperators("232", 8) == ["2*3+2", "2+3*2"]

    def test_solution_2(self, init_variables_282):
        assert init_variables_282().addOperators("105", 5) == ["1*0+5", "10-5"]

    def test_solution_3(self, init_variables_282):
        assert init_variables_282().addOperators("00", 0) == ["0*0", "0+0", "0-0"]

    def test_solution_4(self, init_variables_282):
        assert init_variables_282().addOperators("3456237490", 9191) == []
