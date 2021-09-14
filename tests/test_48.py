#!/usr/bin/env python

import pytest

"""
Test 48. Rotate Image
"""


@pytest.fixture(scope="session")
def init_variables_48():
    from src.leetcode_48_rotate_image import Solution

    solution = Solution()

    def _init_variables_48():
        return solution

    yield _init_variables_48


class TestClass48:
    def test_solution_0(self, init_variables_48):
        assert init_variables_48().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]

    def test_solution_1(self, init_variables_48):
        assert init_variables_48().rotate(
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        ) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    def test_solution_2(self, init_variables_48):
        assert init_variables_48().rotate([[1]]) == [[1]]

    def test_solution_3(self, init_variables_48):
        assert init_variables_48().rotate([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
