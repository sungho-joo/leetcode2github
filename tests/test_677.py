#!/usr/bin/env python

import pytest

"""
Test 677. Map Sum Pairs
"""


@pytest.fixture(scope="session")
def init_variables_677():
    from src.leetcode_677_map_sum_pairs import insert

    solution = insert()

    def _init_variables_677():
        return solution

    yield _init_variables_677


class TestClass677:
    def test_solution_0(self, init_variables_677):
        assert init_variables_677().insert("apple", 3) == None
        assert init_variables_677().sum("ap") == 3
        assert init_variables_677().insert("app", 2) == None
        assert init_variables_677().sum("ap") == 5


#!/usr/bin/env python

import pytest

"""
Test 677. Map Sum Pairs
"""


@pytest.fixture(scope="session")
def init_variables_677():
    from src.leetcode_677_map_sum_pairs import insert

    solution = insert()

    def _init_variables_677():
        return solution

    yield _init_variables_677


class TestClass677:
    def test_solution_0(self, init_variables_677):
        assert init_variables_677().insert("apple", 3) == None
        assert init_variables_677().sum("ap") == 3
        assert init_variables_677().insert("app", 2) == None
        assert init_variables_677().sum("ap") == 5
