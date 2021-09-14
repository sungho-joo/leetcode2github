#!/usr/bin/env python

import pytest

"""
Test 1706. Where Will the Ball Fall
"""


@pytest.fixture(scope="session")
def init_variables_1706():
    from src.leetcode_1706_where_will_the_ball_fall import Solution

    solution = Solution()

    def _init_variables_1706():
        return solution

    yield _init_variables_1706


class TestClass1706:
    def test_solution_0(self, init_variables_1706):
        assert (
            init_variables_1706().findBall(
                [
                    [1, 1, 1, -1, -1],
                    [1, 1, 1, -1, -1],
                    [-1, -1, -1, 1, 1],
                    [1, 1, 1, 1, -1],
                    [-1, -1, -1, -1, -1],
                ]
            )
            == [1, -1, -1, -1, -1]
        )

    def test_solution_1(self, init_variables_1706):
        assert init_variables_1706().findBall([[-1]]) == [-1]

    def test_solution_2(self, init_variables_1706):
        assert init_variables_1706().findBall(
            [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
        ) == [0, 1, 2, 3, 4, -1]
