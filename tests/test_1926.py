#!/usr/bin/env python

import pytest

"""
Test 1926. Nearest Exit from Entrance in Maze
"""


@pytest.fixture(scope="session")
def init_variables_1926():
    from src.leetcode_1926_nearest_exit_from_entrance_in_maze import Solution

    solution = Solution()

    def _init_variables_1926():
        return solution

    yield _init_variables_1926


class TestClass1926:
    def test_solution_0(self, init_variables_1926):
        assert (
            init_variables_1926().nearestExit(
                [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
            )
            == 1
        )

    def test_solution_1(self, init_variables_1926):
        assert (
            init_variables_1926().nearestExit(
                [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]
            )
            == 2
        )

    def test_solution_2(self, init_variables_1926):
        assert init_variables_1926().nearestExit([[".", "+"]], [0, 0]) == -1


#!/usr/bin/env python

import pytest

"""
Test 1926. Nearest Exit from Entrance in Maze
"""


@pytest.fixture(scope="session")
def init_variables_1926():
    from src.leetcode_1926_nearest_exit_from_entrance_in_maze import Solution

    solution = Solution()

    def _init_variables_1926():
        return solution

    yield _init_variables_1926


class TestClass1926:
    def test_solution_0(self, init_variables_1926):
        assert (
            init_variables_1926().nearestExit(
                [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
            )
            == 1
        )

    def test_solution_1(self, init_variables_1926):
        assert (
            init_variables_1926().nearestExit(
                [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]
            )
            == 2
        )

    def test_solution_2(self, init_variables_1926):
        assert init_variables_1926().nearestExit([[".", "+"]], [0, 0]) == -1
