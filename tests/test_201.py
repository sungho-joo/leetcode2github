#!/usr/bin/env python

import pytest

"""
Test 201. Bitwise AND of Numbers Range
"""


@pytest.fixture(scope="session")
def init_variables_201():
    from src.leetcode_201_bitwise_and_of_numbers_range import Solution

    solution = Solution()

    def _init_variables_201():
        return solution

    yield _init_variables_201


class TestClass201:
    def test_solution_0(self, init_variables_201):
        assert init_variables_201().rangeBitwiseAnd(5, 7) == 4

    def test_solution_1(self, init_variables_201):
        assert init_variables_201().rangeBitwiseAnd(0, 0) == 0

    def test_solution_2(self, init_variables_201):
        assert init_variables_201().rangeBitwiseAnd(1, 2147483647) == 0
