#!/usr/bin/env python

import pytest

"""
Test 2076. Process Restricted Friend Requests
"""


@pytest.fixture(scope="session")
def init_variables_2076():
    from src.leetcode_2076_process_restricted_friend_requests import Solution

    solution = Solution()

    def _init_variables_2076():
        return solution

    yield _init_variables_2076


class TestClass2076:
    def test_solution_0(self, init_variables_2076):
        assert init_variables_2076().friendRequests(3, [[0, 1]], [[0, 2], [2, 1]]) == [True, False]

    def test_solution_1(self, init_variables_2076):
        assert init_variables_2076().friendRequests(3, [[0, 1]], [[1, 2], [0, 2]]) == [True, False]

    def test_solution_2(self, init_variables_2076):
        assert init_variables_2076().friendRequests(
            5, [[0, 1], [1, 2], [2, 3]], [[0, 4], [1, 2], [3, 1], [3, 4]]
        ) == [True, False, True, False]
