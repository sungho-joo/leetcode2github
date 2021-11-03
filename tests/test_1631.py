#!/usr/bin/env python

import pytest

"""
Test 1631. Path With Minimum Effort
"""


@pytest.fixture(scope="session")
def init_variables_1631():
    from src.leetcode_1631_path_with_minimum_effort import Solution

    solution = Solution()

    def _init_variables_1631():
        return solution

    yield _init_variables_1631


class TestClass1631:
    def test_solution_0(self, init_variables_1631):
        assert init_variables_1631().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2

    def test_solution_1(self, init_variables_1631):
        assert init_variables_1631().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1

    def test_solution_2(self, init_variables_1631):
        assert (
            init_variables_1631().minimumEffortPath(
                [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
            )
            == 0
        )
