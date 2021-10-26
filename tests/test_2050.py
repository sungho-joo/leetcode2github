#!/usr/bin/env python

import pytest

"""
Test 2050. Parallel Courses III
"""


@pytest.fixture(scope="session")
def init_variables_2050():
    from src.leetcode_2050_parallel_courses_iii import Solution

    solution = Solution()

    def _init_variables_2050():
        return solution

    yield _init_variables_2050


class TestClass2050:
    def test_solution_0(self, init_variables_2050):
        assert init_variables_2050().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]) == 8

    def test_solution_1(self, init_variables_2050):
        assert (
            init_variables_2050().minimumTime(
                5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]
            )
            == 12
        )
