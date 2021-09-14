#!/usr/bin/env python

import pytest

"""
Test 764. Largest Plus Sign
"""


@pytest.fixture(scope="session")
def init_variables_764():
    from src.leetcode_764_largest_plus_sign import Solution

    solution = Solution()

    def _init_variables_764():
        return solution

    yield _init_variables_764


class TestClass764:
    def test_solution_0(self, init_variables_764):
        assert init_variables_764().orderOfLargestPlusSign(5, [[4, 2]]) == 2

    def test_solution_1(self, init_variables_764):
        assert init_variables_764().orderOfLargestPlusSign(1, [[0, 0]]) == 0
