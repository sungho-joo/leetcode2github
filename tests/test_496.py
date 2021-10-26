#!/usr/bin/env python

import pytest

"""
Test 496. Next Greater Element I
"""


@pytest.fixture(scope="session")
def init_variables_496():
    from src.leetcode_496_next_greater_element_i import Solution

    solution = Solution()

    def _init_variables_496():
        return solution

    yield _init_variables_496


class TestClass496:
    def test_solution_0(self, init_variables_496):
        assert init_variables_496().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

    def test_solution_1(self, init_variables_496):
        assert init_variables_496().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
