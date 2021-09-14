#!/usr/bin/env python

import pytest

"""
Test 136. Single Number
"""


@pytest.fixture(scope="session")
def init_variables_136():
    from src.leetcode_136_single_number import Solution

    solution = Solution()

    def _init_variables_136():
        return solution

    yield _init_variables_136


class TestClass136:
    def test_solution_0(self, init_variables_136):
        assert init_variables_136().singleNumber([2, 2, 1]) == 1

    def test_solution_1(self, init_variables_136):
        assert init_variables_136().singleNumber([4, 1, 2, 1, 2]) == 4

    def test_solution_2(self, init_variables_136):
        assert init_variables_136().singleNumber([1]) == 1
