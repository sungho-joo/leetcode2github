#!/usr/bin/env python

import pytest

"""
Test 2037. Minimum Number of Moves to Seat Everyone
"""


@pytest.fixture(scope="session")
def init_variables_2037():
    from src.leetcode_2037_minimum_number_of_moves_to_seat_everyone import Solution

    solution = Solution()

    def _init_variables_2037():
        return solution

    yield _init_variables_2037


class TestClass2037:
    def test_solution_0(self, init_variables_2037):
        assert init_variables_2037().minMovesToSeat([3, 1, 5], [2, 7, 4]) == 4

    def test_solution_1(self, init_variables_2037):
        assert init_variables_2037().minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]) == 7

    def test_solution_2(self, init_variables_2037):
        assert init_variables_2037().minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]) == 4
