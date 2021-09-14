#!/usr/bin/env python

import pytest

"""
Test 1883. Minimum Skips to Arrive at Meeting On Time
"""


@pytest.fixture(scope="session")
def init_variables_1883():
    from src.leetcode_1883_minimum_skips_to_arrive_at_meeting_on_time import Solution

    solution = Solution()

    def _init_variables_1883():
        return solution

    yield _init_variables_1883


class TestClass1883:
    def test_solution_0(self, init_variables_1883):
        assert init_variables_1883().minSkips([1, 3, 2], 4, 2) == 1

    def test_solution_1(self, init_variables_1883):
        assert init_variables_1883().minSkips([7, 3, 5, 5], 2, 10) == 2

    def test_solution_2(self, init_variables_1883):
        assert init_variables_1883().minSkips([7, 3, 5, 5], 1, 10) == -1


#!/usr/bin/env python

import pytest

"""
Test 1883. Minimum Skips to Arrive at Meeting On Time
"""


@pytest.fixture(scope="session")
def init_variables_1883():
    from src.leetcode_1883_minimum_skips_to_arrive_at_meeting_on_time import Solution

    solution = Solution()

    def _init_variables_1883():
        return solution

    yield _init_variables_1883


class TestClass1883:
    def test_solution_0(self, init_variables_1883):
        assert init_variables_1883().minSkips([1, 3, 2], 4, 2) == 1

    def test_solution_1(self, init_variables_1883):
        assert init_variables_1883().minSkips([7, 3, 5, 5], 2, 10) == 2

    def test_solution_2(self, init_variables_1883):
        assert init_variables_1883().minSkips([7, 3, 5, 5], 1, 10) == -1
