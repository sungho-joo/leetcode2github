#!/usr/bin/env python

import pytest

"""
Test 2001. Number of Pairs of Interchangeable Rectangles
"""


@pytest.fixture(scope="session")
def init_variables_2001():
    from src.leetcode_2001_number_of_pairs_of_interchangeable_rectangles import Solution

    solution = Solution()

    def _init_variables_2001():
        return solution

    yield _init_variables_2001


class TestClass2001:
    def test_solution_0(self, init_variables_2001):
        assert (
            init_variables_2001().interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]) == 6
        )

    def test_solution_1(self, init_variables_2001):
        assert init_variables_2001().interchangeableRectangles([[4, 5], [7, 8]]) == 0
