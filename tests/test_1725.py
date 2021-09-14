#!/usr/bin/env python

import pytest

"""
Test 1725. Number Of Rectangles That Can Form The Largest Square
"""


@pytest.fixture(scope="session")
def init_variables_1725():
    from src.leetcode_1725_number_of_rectangles_that_can_form_the_largest_square import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1725():
        return solution

    yield _init_variables_1725


class TestClass1725:
    def test_solution_0(self, init_variables_1725):
        assert init_variables_1725().countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]) == 3

    def test_solution_1(self, init_variables_1725):
        assert init_variables_1725().countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]) == 3
