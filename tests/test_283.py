#!/usr/bin/env python

import pytest

"""
Test 283. Move Zeroes
"""


@pytest.fixture(scope="session")
def init_variables_283():
    from src.leetcode_283_move_zeroes import Solution

    solution = Solution()

    def _init_variables_283():
        return solution

    yield _init_variables_283


class TestClass283:
    def test_solution_0(self, init_variables_283):
        assert init_variables_283().moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

    def test_solution_1(self, init_variables_283):
        assert init_variables_283().moveZeroes([0]) == [0]
