#!/usr/bin/env python

import pytest

"""
Test 174. Dungeon Game
"""


@pytest.fixture(scope="session")
def init_variables_174():
    from src.leetcode_174_dungeon_game import Solution

    solution = Solution()

    def _init_variables_174():
        return solution

    yield _init_variables_174


class TestClass174:
    def test_solution_0(self, init_variables_174):
        assert init_variables_174().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7

    def test_solution_1(self, init_variables_174):
        assert init_variables_174().calculateMinimumHP([[0]]) == 1
