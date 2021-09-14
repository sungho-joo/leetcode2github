#!/usr/bin/env python

import pytest

"""
Test 303. Range Sum Query - Immutable
"""


@pytest.fixture(scope="session")
def init_variables_303():
    from src.leetcode_303_range_sum_query_immutable import NumArray

    solution = NumArray([-2, 0, 3, -5, 2, -1])

    def _init_variables_303():
        return solution

    yield _init_variables_303


class TestClass303:
    def test_solution_0(self, init_variables_303):
        assert init_variables_303().sumRange(0, 2) == 1
        assert init_variables_303().sumRange(2, 5) == -1
        assert init_variables_303().sumRange(0, 5) == -3


#!/usr/bin/env python

import pytest

"""
Test 303. Range Sum Query - Immutable
"""


@pytest.fixture(scope="session")
def init_variables_303():
    from src.leetcode_303_range_sum_query_immutable import NumArray

    solution = NumArray([-2, 0, 3, -5, 2, -1])

    def _init_variables_303():
        return solution

    yield _init_variables_303


class TestClass303:
    def test_solution_0(self, init_variables_303):
        assert init_variables_303().sumRange(0, 2) == 1
        assert init_variables_303().sumRange(2, 5) == -1
        assert init_variables_303().sumRange(0, 5) == -3
