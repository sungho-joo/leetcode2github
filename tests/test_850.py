#!/usr/bin/env python

import pytest

"""
Test 850. Rectangle Area II
"""


@pytest.fixture(scope="session")
def init_variables_850():
    from src.leetcode_850_rectangle_area_ii import Solution

    solution = Solution()

    def _init_variables_850():
        return solution

    yield _init_variables_850


class TestClass850:
    def test_solution_0(self, init_variables_850):
        assert init_variables_850().rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]) == 6

    def test_solution_1(self, init_variables_850):
        assert init_variables_850().rectangleArea([[0, 0, 1000000000, 1000000000]]) == 49
