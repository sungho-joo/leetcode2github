#!/usr/bin/env python

import pytest

"""
Test 537. Complex Number Multiplication
"""


@pytest.fixture(scope="session")
def init_variables_537():
    from src.leetcode_537_complex_number_multiplication import Solution

    solution = Solution()

    def _init_variables_537():
        return solution

    yield _init_variables_537


class TestClass537:
    def test_solution_0(self, init_variables_537):
        assert init_variables_537().complexNumberMultiply("1+1i", "1+1i") == "0+2i"

    def test_solution_1(self, init_variables_537):
        assert init_variables_537().complexNumberMultiply("1+-1i", "1+-1i") == "0+-2i"
