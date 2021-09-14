#!/usr/bin/env python

import pytest

"""
Test 1975. Maximum Matrix Sum
"""


@pytest.fixture(scope="session")
def init_variables_1975():
    from src.leetcode_1975_maximum_matrix_sum import Solution

    solution = Solution()

    def _init_variables_1975():
        return solution

    yield _init_variables_1975


class TestClass1975:
    def test_solution_0(self, init_variables_1975):
        assert init_variables_1975().maxMatrixSum([[1, -1], [-1, 1]]) == 4

    def test_solution_1(self, init_variables_1975):
        assert init_variables_1975().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
