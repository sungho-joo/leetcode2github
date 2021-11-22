#!/usr/bin/env python

import pytest

"""
Test 260. Single Number III
"""


@pytest.fixture(scope="session")
def init_variables_260():
    from src.leetcode_260_single_number_iii import Solution

    solution = Solution()

    def _init_variables_260():
        return solution

    yield _init_variables_260


class TestClass260:
    def test_solution_0(self, init_variables_260):
        assert init_variables_260().singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5]

    def test_solution_1(self, init_variables_260):
        assert init_variables_260().singleNumber([-1, 0]) == [-1, 0]

    def test_solution_2(self, init_variables_260):
        assert init_variables_260().singleNumber([0, 1]) == [1, 0]
