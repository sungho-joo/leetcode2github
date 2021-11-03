#!/usr/bin/env python

import pytest

"""
Test 2059. Minimum Operations to Convert Number
"""


@pytest.fixture(scope="session")
def init_variables_2059():
    from src.leetcode_2059_minimum_operations_to_convert_number import Solution

    solution = Solution()

    def _init_variables_2059():
        return solution

    yield _init_variables_2059


class TestClass2059:
    def test_solution_0(self, init_variables_2059):
        assert init_variables_2059().minimumOperations([1, 3], 6, 4) == 2

    def test_solution_1(self, init_variables_2059):
        assert init_variables_2059().minimumOperations([2, 4, 12], 2, 12) == 2

    def test_solution_2(self, init_variables_2059):
        assert init_variables_2059().minimumOperations([3, 5, 7], 0, -4) == 2

    def test_solution_3(self, init_variables_2059):
        assert init_variables_2059().minimumOperations([2, 8, 16], 0, 1) == -1

    def test_solution_4(self, init_variables_2059):
        assert init_variables_2059().minimumOperations([1], 0, 3) == 3
