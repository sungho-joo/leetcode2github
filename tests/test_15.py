#!/usr/bin/env python

import pytest

"""
Test 15. 3Sum
"""


@pytest.fixture(scope="session")
def init_variables_15():
    from src.leetcode_15_3sum import Solution

    solution = Solution()

    def _init_variables_15():
        return solution

    yield _init_variables_15


class TestClass15:
    def test_solution_0(self, init_variables_15):
        assert init_variables_15().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    def test_solution_1(self, init_variables_15):
        assert init_variables_15().threeSum([]) == []

    def test_solution_2(self, init_variables_15):
        assert init_variables_15().threeSum([0]) == []
