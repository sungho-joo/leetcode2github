#!/usr/bin/env python

import pytest

"""
Test 190. Reverse Bits
"""


@pytest.fixture(scope="session")
def init_variables_190():
    from src.leetcode_190_reverse_bits import Solution
    solution = Solution()

    def _init_variables_190():
        return solution

    yield _init_variables_190

class TestClass190:
    def test_solution_0(self, init_variables_190):
        assert init_variables_190().                            reverseBits(00000010100101000001111010011100) ==    964176192 (00111001011110000010100101000000)

    def test_solution_1(self, init_variables_190):
        assert init_variables_190().                            reverseBits(11111111111111111111111111111101) ==   3221225471 (10111111111111111111111111111111)
