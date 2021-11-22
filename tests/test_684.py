#!/usr/bin/env python

import pytest

"""
Test 684. Redundant Connection
"""


@pytest.fixture(scope="session")
def init_variables_684():
    from src.leetcode_684_redundant_connection import Solution

    solution = Solution()

    def _init_variables_684():
        return solution

    yield _init_variables_684


class TestClass684:
    def test_solution_0(self, init_variables_684):
        assert init_variables_684().findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]

    def test_solution_1(self, init_variables_684):
        assert init_variables_684().findRedundantConnection(
            [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        ) == [1, 4]
