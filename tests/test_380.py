#!/usr/bin/env python

import pytest

"""
Test 380. Insert Delete GetRandom O(1)
"""


@pytest.fixture(scope="session")
def init_variables_380():
    from src.leetcode_380_insert_delete_getrandom_o1 import insert

    solution = insert()

    def _init_variables_380():
        return solution

    yield _init_variables_380


class TestClass380:
    def test_solution_0(self, init_variables_380):
        assert init_variables_380().insert(1) == True
        assert init_variables_380().remove(2) == False
        assert init_variables_380().insert(2) == True
        assert init_variables_380().getRandom() == 2
        assert init_variables_380().remove(1) == True
        assert init_variables_380().insert(2) == False
        assert init_variables_380().getRandom() == 2
