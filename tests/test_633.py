#!/usr/bin/env python

import pytest

"""
Test 633. Sum of Square Numbers
"""


@pytest.fixture(scope="session")
def init_variables_633():
    from src.leetcode_633_sum_of_square_numbers import Solution

    solution = Solution()

    def _init_variables_633():
        return solution

    yield _init_variables_633


class TestClass633:
    def test_solution_0(self, init_variables_633):
        assert init_variables_633().judgeSquareSum(5)

    def test_solution_1(self, init_variables_633):
        assert not init_variables_633().judgeSquareSum(3)

    def test_solution_2(self, init_variables_633):
        assert init_variables_633().judgeSquareSum(4)

    def test_solution_3(self, init_variables_633):
        assert init_variables_633().judgeSquareSum(2)

    def test_solution_4(self, init_variables_633):
        assert init_variables_633().judgeSquareSum(1)
