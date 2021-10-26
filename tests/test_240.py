#!/usr/bin/env python

import pytest

"""
Test 240. Search a 2D Matrix II
"""


@pytest.fixture(scope="session")
def init_variables_240():
    from src.leetcode_240_search_a_2d_matrix_ii import Solution

    solution = Solution()

    def _init_variables_240():
        return solution

    yield _init_variables_240


class TestClass240:
    def test_solution_0(self, init_variables_240):
        assert init_variables_240().searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
        )

    def test_solution_1(self, init_variables_240):
        assert not init_variables_240().searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
        )
