#!/usr/bin/env python

import pytest

"""
Test 70. Climbing Stairs
"""


@pytest.fixture(scope="session")
def init_variables_70():
    from src.leetcode_70_climbing_stairs import Solution

    solution = Solution()

    def _init_variables_70():
        return solution

    yield _init_variables_70


class TestClass70:
    def test_solution_0(self, init_variables_70):
        assert init_variables_70().climbStairs(2) == 2

    def test_solution_1(self, init_variables_70):
        assert init_variables_70().climbStairs(3) == 3
