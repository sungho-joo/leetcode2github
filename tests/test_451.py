#!/usr/bin/env python

import pytest

"""
Test 451. Sort Characters By Frequency
"""


@pytest.fixture(scope="session")
def init_variables_451():
    from src.leetcode_451_sort_characters_by_frequency import Solution

    solution = Solution()

    def _init_variables_451():
        return solution

    yield _init_variables_451


class TestClass451:
    def test_solution_0(self, init_variables_451):
        assert init_variables_451().frequencySort("tree") == "eert"

    def test_solution_1(self, init_variables_451):
        assert init_variables_451().frequencySort("cccaaa") == "aaaccc"

    def test_solution_2(self, init_variables_451):
        assert init_variables_451().frequencySort("Aabb") == "bbAa"
