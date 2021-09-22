#!/usr/bin/env python

import pytest

"""
Test 54. Spiral Matrix
"""


@pytest.fixture(scope="session")
def init_variables_54():
    from src.leetcode_54_spiral_matrix import Solution

    solution = Solution()

    def _init_variables_54():
        return solution

    yield _init_variables_54


class TestClass54:
    def test_solution_0(self, init_variables_54):
        assert init_variables_54().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
            1,
            2,
            3,
            6,
            9,
            8,
            7,
            4,
            5,
        ]

    def test_solution_1(self, init_variables_54):
        assert init_variables_54().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
            1,
            2,
            3,
            4,
            8,
            12,
            11,
            10,
            9,
            5,
            6,
            7,
        ]
