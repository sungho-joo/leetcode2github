#!/usr/bin/env python

import pytest

"""
Test 653. Two Sum IV - Input is a BST
"""


@pytest.fixture(scope="session")
def init_variables_653():
    from src.leetcode_653_two_sum_iv_input_is_a_bst import Solution

    solution = Solution()

    def _init_variables_653():
        return solution

    yield _init_variables_653


class TestClass653:
    def test_solution_0(self, init_variables_653):
        assert init_variables_653().findTarget([5, 3, 6, 2, 4, None, 7], 9)

    def test_solution_1(self, init_variables_653):
        assert not init_variables_653().findTarget([5, 3, 6, 2, 4, None, 7], 28)

    def test_solution_2(self, init_variables_653):
        assert init_variables_653().findTarget([2, 1, 3], 4)

    def test_solution_3(self, init_variables_653):
        assert not init_variables_653().findTarget([2, 1, 3], 1)

    def test_solution_4(self, init_variables_653):
        assert init_variables_653().findTarget([2, 1, 3], 3)
