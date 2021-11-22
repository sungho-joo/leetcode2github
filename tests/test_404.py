#!/usr/bin/env python

import pytest

"""
Test 404. Sum of Left Leaves
"""


@pytest.fixture(scope="session")
def init_variables_404():
    from src.leetcode_404_sum_of_left_leaves import Solution

    solution = Solution()

    def _init_variables_404():
        return solution

    yield _init_variables_404


class TestClass404:
    def test_solution_0(self, init_variables_404):
        assert init_variables_404().sumOfLeftLeaves([3, 9, 20, None, None, 15, 7]) == 24

    def test_solution_1(self, init_variables_404):
        assert init_variables_404().sumOfLeftLeaves([1]) == 0
