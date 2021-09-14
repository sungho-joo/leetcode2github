#!/usr/bin/env python

import pytest

"""
Test 56. Merge Intervals
"""


@pytest.fixture(scope="session")
def init_variables_56():
    from src.leetcode_56_merge_intervals import Solution

    solution = Solution()

    def _init_variables_56():
        return solution

    yield _init_variables_56


class TestClass56:
    def test_solution_0(self, init_variables_56):
        assert init_variables_56().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
            [1, 6],
            [8, 10],
            [15, 18],
        ]

    def test_solution_1(self, init_variables_56):
        assert init_variables_56().merge([[1, 4], [4, 5]]) == [[1, 5]]
