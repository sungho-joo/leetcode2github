#!/usr/bin/env python

import pytest

"""
Test 2054. Two Best Non-Overlapping Events
"""


@pytest.fixture(scope="session")
def init_variables_2054():
    from src.leetcode_2054_two_best_non_overlapping_events import Solution

    solution = Solution()

    def _init_variables_2054():
        return solution

    yield _init_variables_2054


class TestClass2054:
    def test_solution_0(self, init_variables_2054):
        assert init_variables_2054().maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4

    def test_solution_1(self, init_variables_2054):
        assert init_variables_2054().maxTwoEvents([[1, 3, 2], [4, 5, 2], [1, 5, 5]]) == 5

    def test_solution_2(self, init_variables_2054):
        assert init_variables_2054().maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]) == 8
