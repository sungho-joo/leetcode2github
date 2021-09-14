#!/usr/bin/env python

import pytest

"""
Test 1824. Minimum Sideway Jumps
"""


@pytest.fixture(scope="session")
def init_variables_1824():
    from src.leetcode_1824_minimum_sideway_jumps import Solution

    solution = Solution()

    def _init_variables_1824():
        return solution

    yield _init_variables_1824


class TestClass1824:
    def test_solution_0(self, init_variables_1824):
        assert init_variables_1824().minSideJumps([0, 1, 2, 3, 0]) == 2

    def test_solution_1(self, init_variables_1824):
        assert init_variables_1824().minSideJumps([0, 1, 1, 3, 3, 0]) == 0

    def test_solution_2(self, init_variables_1824):
        assert init_variables_1824().minSideJumps([0, 2, 1, 0, 3, 0]) == 2
