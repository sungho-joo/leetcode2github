#!/usr/bin/env python

import pytest

"""
Test 198. House Robber
"""


@pytest.fixture(scope="session")
def init_variables_198():
    from src.leetcode_198_house_robber import Solution

    solution = Solution()

    def _init_variables_198():
        return solution

    yield _init_variables_198


class TestClass198:
    def test_solution_0(self, init_variables_198):
        assert init_variables_198().rob([1, 2, 3, 1]) == 4

    def test_solution_1(self, init_variables_198):
        assert init_variables_198().rob([2, 7, 9, 3, 1]) == 12
