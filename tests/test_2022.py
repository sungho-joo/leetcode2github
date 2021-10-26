#!/usr/bin/env python

import pytest

"""
Test 2022. Convert 1D Array Into 2D Array
"""


@pytest.fixture(scope="session")
def init_variables_2022():
    from src.leetcode_2022_convert_1d_array_into_2d_array import Solution
    solution = Solution()

    def _init_variables_2022():
        return solution

    yield _init_variables_2022

class TestClass2022:
    def test_solution_0(self, init_variables_2022):
        assert init_variables_2022().                            construct2DArray([1,2,3,4], 2, 2) == [[1,2],[3,4]]

    def test_solution_1(self, init_variables_2022):
        assert init_variables_2022().                            construct2DArray([1,2,3], 1, 3) == [[1,2,3]]

    def test_solution_2(self, init_variables_2022):
        assert init_variables_2022().                            construct2DArray([1,2], 1, 1) == []

    def test_solution_3(self, init_variables_2022):
        assert init_variables_2022().                            construct2DArray([3], 1, 2) == []
