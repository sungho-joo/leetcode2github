#!/usr/bin/env python

import pytest

"""
Test 1137. N-th Tribonacci Number
"""


@pytest.fixture(scope="session")
def init_variables_1137():
    from src.leetcode_1137_n_th_tribonacci_number import Solution

    solution = Solution()

    def _init_variables_1137():
        return solution

    yield _init_variables_1137


class TestClass1137:
    def test_solution_0(self, init_variables_1137):
        assert init_variables_1137().tribonacci(4) == 4

    def test_solution_1(self, init_variables_1137):
        assert init_variables_1137().tribonacci(25) == 1389537
