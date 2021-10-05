#!/usr/bin/env python

import pytest

"""
Test 1293. Shortest Path in a Grid with Obstacles Elimination
"""


@pytest.fixture(scope="session")
def init_variables_1293():
    from src.leetcode_1293_shortest_path_in_a_grid_with_obstacles_elimination import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1293():
        return solution

    yield _init_variables_1293


class TestClass1293:
    def test_solution_0(self, init_variables_1293):
        assert (
            init_variables_1293().shortestPath(
                [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1
            )
            == 6
        )

    def test_solution_1(self, init_variables_1293):
        assert init_variables_1293().shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1) == -1
