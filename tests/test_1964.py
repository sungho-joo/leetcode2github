#!/usr/bin/env python

import pytest

"""
Test 1964. Find the Longest Valid Obstacle Course at Each Position
"""


@pytest.fixture(scope="session")
def init_variables_1964():
    from src.leetcode_1964_find_the_longest_valid_obstacle_course_at_each_position import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1964():
        return solution

    yield _init_variables_1964


class TestClass1964:
    def test_solution_0(self, init_variables_1964):
        assert init_variables_1964().longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]

    def test_solution_1(self, init_variables_1964):
        assert init_variables_1964().longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]

    def test_solution_2(self, init_variables_1964):
        assert init_variables_1964().longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [
            1,
            1,
            2,
            3,
            2,
            2,
        ]


#!/usr/bin/env python

import pytest

"""
Test 1964. Find the Longest Valid Obstacle Course at Each Position
"""


@pytest.fixture(scope="session")
def init_variables_1964():
    from src.leetcode_1964_find_the_longest_valid_obstacle_course_at_each_position import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1964():
        return solution

    yield _init_variables_1964


class TestClass1964:
    def test_solution_0(self, init_variables_1964):
        assert init_variables_1964().longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]

    def test_solution_1(self, init_variables_1964):
        assert init_variables_1964().longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]

    def test_solution_2(self, init_variables_1964):
        assert init_variables_1964().longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [
            1,
            1,
            2,
            3,
            2,
            2,
        ]
