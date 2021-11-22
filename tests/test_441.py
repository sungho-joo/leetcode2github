#!/usr/bin/env python

import pytest

"""
Test 441. Arranging Coins
"""


@pytest.fixture(scope="session")
def init_variables_441():
    from src.leetcode_441_arranging_coins import Solution

    solution = Solution()

    def _init_variables_441():
        return solution

    yield _init_variables_441


class TestClass441:
    def test_solution_0(self, init_variables_441):
        assert init_variables_441().arrangeCoins(5) == 2

    def test_solution_1(self, init_variables_441):
        assert init_variables_441().arrangeCoins(8) == 3
