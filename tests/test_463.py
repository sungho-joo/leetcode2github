#!/usr/bin/env python

import pytest

"""
Test 463. Island Perimeter
"""


@pytest.fixture(scope="session")
def init_variables_463():
    from src.leetcode_463_island_perimeter import Solution

    solution = Solution()

    def _init_variables_463():
        return solution

    yield _init_variables_463


class TestClass463:
    def test_solution_0(self, init_variables_463):
        assert (
            init_variables_463().islandPerimeter(
                [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
            )
            == 16
        )

    def test_solution_1(self, init_variables_463):
        assert init_variables_463().islandPerimeter([[1]]) == 4

    def test_solution_2(self, init_variables_463):
        assert init_variables_463().islandPerimeter([[1, 0]]) == 4
