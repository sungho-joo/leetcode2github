#!/usr/bin/env python

import pytest

"""
Test 279. Perfect Squares
"""


@pytest.fixture(scope="session")
def init_variables_279():
    from src.leetcode_279_perfect_squares import Solution

    solution = Solution()

    def _init_variables_279():
        return solution

    yield _init_variables_279


class TestClass279:
    def test_solution_0(self, init_variables_279):
        assert init_variables_279().numSquares(12) == 3

    def test_solution_1(self, init_variables_279):
        assert init_variables_279().numSquares(13) == 2
