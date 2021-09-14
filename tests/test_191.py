#!/usr/bin/env python

import pytest

"""
Test 191. Number of 1 Bits
"""


@pytest.fixture(scope="session")
def init_variables_191():
    from src.leetcode_191_number_of_1_bits import Solution
    solution = Solution()

    def _init_variables_191():
        return solution

    yield _init_variables_191

class TestClass191:
    def test_solution_0(self, init_variables_191):
        assert init_variables_191().                            hammingWeight(00000000000000000000000000001011) == 3

    def test_solution_1(self, init_variables_191):
        assert init_variables_191().                            hammingWeight(00000000000000000000000010000000) == 1

    def test_solution_2(self, init_variables_191):
        assert init_variables_191().                            hammingWeight(11111111111111111111111111111101) == 31
