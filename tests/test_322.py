#!/usr/bin/env python

import pytest

"""
Test 322. Coin Change
"""


@pytest.fixture(scope="session")
def init_variables_322():
    from src.leetcode_322_coin_change import Solution

    solution = Solution()

    def _init_variables_322():
        return solution

    yield _init_variables_322


class TestClass322:
    def test_solution_0(self, init_variables_322):
        assert init_variables_322().coinChange([1, 2, 5], 11) == 3

    def test_solution_1(self, init_variables_322):
        assert init_variables_322().coinChange([2], 3) == -1

    def test_solution_2(self, init_variables_322):
        assert init_variables_322().coinChange([1], 0) == 0

    def test_solution_3(self, init_variables_322):
        assert init_variables_322().coinChange([1], 1) == 1

    def test_solution_4(self, init_variables_322):
        assert init_variables_322().coinChange([1], 2) == 2
