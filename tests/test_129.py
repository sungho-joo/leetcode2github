#!/usr/bin/env python

import pytest

"""
Test 129. Sum Root to Leaf Numbers
"""


@pytest.fixture(scope="session")
def init_variables_129():
    from src.leetcode_129_sum_root_to_leaf_numbers import Solution

    solution = Solution()

    def _init_variables_129():
        return solution

    yield _init_variables_129


class TestClass129:
    def test_solution_0(self, init_variables_129):
        assert init_variables_129().sumNumbers([1, 2, 3]) == 25

    def test_solution_1(self, init_variables_129):
        assert init_variables_129().sumNumbers([4, 9, 0, 5, 1]) == 1026
