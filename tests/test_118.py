#!/usr/bin/env python

import pytest

"""
Test 118. Pascal's Triangle
"""


@pytest.fixture(scope="session")
def init_variables_118():
    from src.leetcode_118_pascals_triangle import Solution

    solution = Solution()

    def _init_variables_118():
        return solution

    yield _init_variables_118


class TestClass118:
    def test_solution_0(self, init_variables_118):
        assert init_variables_118().generate(5) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]

    def test_solution_1(self, init_variables_118):
        assert init_variables_118().generate(1) == [[1]]
