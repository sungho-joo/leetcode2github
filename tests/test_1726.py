#!/usr/bin/env python

import pytest

"""
Test 1726. Tuple with Same Product
"""


@pytest.fixture(scope="session")
def init_variables_1726():
    from src.leetcode_1726_tuple_with_same_product import Solution

    solution = Solution()

    def _init_variables_1726():
        return solution

    yield _init_variables_1726


class TestClass1726:
    def test_solution_0(self, init_variables_1726):
        assert init_variables_1726().tupleSameProduct([2, 3, 4, 6]) == 8

    def test_solution_1(self, init_variables_1726):
        assert init_variables_1726().tupleSameProduct([1, 2, 4, 5, 10]) == 16

    def test_solution_2(self, init_variables_1726):
        assert init_variables_1726().tupleSameProduct([2, 3, 4, 6, 8, 12]) == 40

    def test_solution_3(self, init_variables_1726):
        assert init_variables_1726().tupleSameProduct([2, 3, 5, 7]) == 0
