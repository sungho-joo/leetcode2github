#!/usr/bin/env python

import pytest

"""
Test 1514. Path with Maximum Probability
"""


@pytest.fixture(scope="session")
def init_variables_1514():
    from src.leetcode_1514_path_with_maximum_probability import Solution

    solution = Solution()

    def _init_variables_1514():
        return solution

    yield _init_variables_1514


class TestClass1514:
    def test_solution_0(self, init_variables_1514):
        assert (
            init_variables_1514().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2)
            == 0.25000
        )

    def test_solution_1(self, init_variables_1514):
        assert (
            init_variables_1514().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2)
            == 0.30000
        )

    def test_solution_2(self, init_variables_1514):
        assert init_variables_1514().maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0.00000
