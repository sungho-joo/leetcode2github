#!/usr/bin/env python

import pytest

"""
Test 437. Path Sum III
"""


@pytest.fixture(scope="session")
def init_variables_437():
    from src.leetcode_437_path_sum_iii import Solution

    solution = Solution()

    def _init_variables_437():
        return solution

    yield _init_variables_437


class TestClass437:
    def test_solution_0(self, init_variables_437):
        assert init_variables_437().pathSum([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8) == 3

    def test_solution_1(self, init_variables_437):
        assert init_variables_437().pathSum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22) == 3
