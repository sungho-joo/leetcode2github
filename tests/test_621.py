#!/usr/bin/env python

import pytest

"""
Test 621. Task Scheduler
"""


@pytest.fixture(scope="session")
def init_variables_621():
    from src.leetcode_621_task_scheduler import Solution

    solution = Solution()

    def _init_variables_621():
        return solution

    yield _init_variables_621


class TestClass621:
    def test_solution_0(self, init_variables_621):
        assert init_variables_621().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8

    def test_solution_1(self, init_variables_621):
        assert init_variables_621().leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6

    def test_solution_2(self, init_variables_621):
        assert (
            init_variables_621().leastInterval(
                ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
            )
            == 16
        )
