#!/usr/bin/env python

import pytest

"""
Test 1110. Delete Nodes And Return Forest
"""


@pytest.fixture(scope="session")
def init_variables_1110():
    from src.leetcode_1110_delete_nodes_and_return_forest import Solution

    solution = Solution()

    def _init_variables_1110():
        return solution

    yield _init_variables_1110


class TestClass1110:
    def test_solution_0(self, init_variables_1110):
        assert init_variables_1110().delNodes([1, 2, 3, 4, 5, 6, 7], [3, 5]) == [
            [1, 2, None, 4],
            [6],
            [7],
        ]

    def test_solution_1(self, init_variables_1110):
        assert init_variables_1110().delNodes([1, 2, 4, None, 3], [3]) == [[1, 2, 4]]
