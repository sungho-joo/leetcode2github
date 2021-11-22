#!/usr/bin/env python

import pytest

"""
Test 2065. Maximum Path Quality of a Graph
"""


@pytest.fixture(scope="session")
def init_variables_2065():
    from src.leetcode_2065_maximum_path_quality_of_a_graph import Solution

    solution = Solution()

    def _init_variables_2065():
        return solution

    yield _init_variables_2065


class TestClass2065:
    def test_solution_0(self, init_variables_2065):
        assert (
            init_variables_2065().maximalPathQuality(
                [0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49
            )
            == 75
        )

    def test_solution_1(self, init_variables_2065):
        assert (
            init_variables_2065().maximalPathQuality(
                [5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30
            )
            == 25
        )

    def test_solution_2(self, init_variables_2065):
        assert (
            init_variables_2065().maximalPathQuality(
                [1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50
            )
            == 7
        )

    def test_solution_3(self, init_variables_2065):
        assert init_variables_2065().maximalPathQuality([0, 1, 2], [[1, 2, 10]], 10) == 0
