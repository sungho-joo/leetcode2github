#!/usr/bin/env python

import pytest

"""
Test 1992. Find All Groups of Farmland
"""


@pytest.fixture(scope="session")
def init_variables_1992():
    from src.leetcode_1992_find_all_groups_of_farmland import Solution

    solution = Solution()

    def _init_variables_1992():
        return solution

    yield _init_variables_1992


class TestClass1992:
    def test_solution_0(self, init_variables_1992):
        assert init_variables_1992().findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [
            [0, 0, 0, 0],
            [1, 1, 2, 2],
        ]

    def test_solution_1(self, init_variables_1992):
        assert init_variables_1992().findFarmland([[1, 1], [1, 1]]) == [[0, 0, 1, 1]]

    def test_solution_2(self, init_variables_1992):
        assert init_variables_1992().findFarmland([[0]]) == []
