#!/usr/bin/env python

import pytest

"""
Test 55. Jump Game
"""


@pytest.fixture(scope="session")
def init_variables_55():
    from src.leetcode_55_jump_game import Solution

    solution = Solution()

    def _init_variables_55():
        return solution

    yield _init_variables_55


class TestClass55:
    def test_solution_0(self, init_variables_55):
        assert init_variables_55().canJump([2, 3, 1, 1, 4])

    def test_solution_1(self, init_variables_55):
        assert not init_variables_55().canJump([3, 2, 1, 0, 4])
