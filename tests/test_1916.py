#!/usr/bin/env python

import pytest

"""
Test 1916. Count Ways to Build Rooms in an Ant Colony
"""


@pytest.fixture(scope="session")
def init_variables_1916():
    from src.leetcode_1916_count_ways_to_build_rooms_in_an_ant_colony import Solution

    solution = Solution()

    def _init_variables_1916():
        return solution

    yield _init_variables_1916


class TestClass1916:
    def test_solution_0(self, init_variables_1916):
        assert init_variables_1916().waysToBuildRooms([-1, 0, 1]) == 1

    def test_solution_1(self, init_variables_1916):
        assert init_variables_1916().waysToBuildRooms([-1, 0, 0, 1, 2]) == 6


#!/usr/bin/env python

import pytest

"""
Test 1916. Count Ways to Build Rooms in an Ant Colony
"""


@pytest.fixture(scope="session")
def init_variables_1916():
    from src.leetcode_1916_count_ways_to_build_rooms_in_an_ant_colony import Solution

    solution = Solution()

    def _init_variables_1916():
        return solution

    yield _init_variables_1916


class TestClass1916:
    def test_solution_0(self, init_variables_1916):
        assert init_variables_1916().waysToBuildRooms([-1, 0, 1]) == 1

    def test_solution_1(self, init_variables_1916):
        assert init_variables_1916().waysToBuildRooms([-1, 0, 0, 1, 2]) == 6
