#!/usr/bin/env python

import pytest

"""
Test 1997. First Day Where You Have Been in All the Rooms
"""


@pytest.fixture(scope="session")
def init_variables_1997():
    from src.leetcode_1997_first_day_where_you_have_been_in_all_the_rooms import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1997():
        return solution

    yield _init_variables_1997


class TestClass1997:
    def test_solution_0(self, init_variables_1997):
        assert init_variables_1997().firstDayBeenInAllRooms([0, 0]) == 2

    def test_solution_1(self, init_variables_1997):
        assert init_variables_1997().firstDayBeenInAllRooms([0, 0, 2]) == 6

    def test_solution_2(self, init_variables_1997):
        assert init_variables_1997().firstDayBeenInAllRooms([0, 1, 2, 0]) == 6
