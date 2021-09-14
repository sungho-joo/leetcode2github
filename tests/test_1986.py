#!/usr/bin/env python

import pytest

"""
Test 1986. Minimum Number of Work Sessions to Finish the Tasks
"""


@pytest.fixture(scope="session")
def init_variables_1986():
    from src.leetcode_1986_minimum_number_of_work_sessions_to_finish_the_tasks import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1986():
        return solution

    yield _init_variables_1986


class TestClass1986:
    def test_solution_0(self, init_variables_1986):
        assert init_variables_1986().minSessions([1, 2, 3], 3) == 2

    def test_solution_1(self, init_variables_1986):
        assert init_variables_1986().minSessions([3, 1, 3, 1, 1], 8) == 2

    def test_solution_2(self, init_variables_1986):
        assert init_variables_1986().minSessions([1, 2, 3, 4, 5], 15) == 1
