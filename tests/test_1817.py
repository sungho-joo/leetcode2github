#!/usr/bin/env python

import pytest

"""
Test 1817. Finding the Users Active Minutes
"""


@pytest.fixture(scope="session")
def init_variables_1817():
    from src.leetcode_1817_finding_the_users_active_minutes import Solution

    solution = Solution()

    def _init_variables_1817():
        return solution

    yield _init_variables_1817


class TestClass1817:
    def test_solution_0(self, init_variables_1817):
        assert init_variables_1817().findingUsersActiveMinutes(
            [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5
        ) == [0, 2, 0, 0, 0]

    def test_solution_1(self, init_variables_1817):
        assert init_variables_1817().findingUsersActiveMinutes([[1, 1], [2, 2], [2, 3]], 4) == [
            1,
            1,
            0,
            0,
        ]
