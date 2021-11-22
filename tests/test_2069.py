#!/usr/bin/env python

import pytest

"""
Test 2069. Walking Robot Simulation II
"""


@pytest.fixture(scope="session")
def init_variables_2069():
    from src.leetcode_2069_walking_robot_simulation_ii import Robot

    solution = Robot(6, 3)

    def _init_variables_2069():
        return solution

    yield _init_variables_2069


class TestClass2069:
    def test_solution_0(self, init_variables_2069):
        assert init_variables_2069().step(2) == None
        assert init_variables_2069().step(2) == None
        assert init_variables_2069().getPos() == [4, 0]
        assert init_variables_2069().getDir() == East
        assert init_variables_2069().step(2) == None
        assert init_variables_2069().step(1) == None
        assert init_variables_2069().step(4) == None
        assert init_variables_2069().getPos() == [1, 2]
        assert init_variables_2069().getDir() == West
