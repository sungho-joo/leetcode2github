#!/usr/bin/env python

import pytest

"""
Test 1962. Remove Stones to Minimize the Total
"""


@pytest.fixture(scope="session")
def init_variables_1962():
    from src.leetcode_1962_remove_stones_to_minimize_the_total import Solution

    solution = Solution()

    def _init_variables_1962():
        return solution

    yield _init_variables_1962


class TestClass1962:
    def test_solution_0(self, init_variables_1962):
        assert init_variables_1962().minStoneSum([5, 4, 9], 2) == 12

    def test_solution_1(self, init_variables_1962):
        assert init_variables_1962().minStoneSum([4, 3, 6, 7], 3) == 12


#!/usr/bin/env python

import pytest

"""
Test 1962. Remove Stones to Minimize the Total
"""


@pytest.fixture(scope="session")
def init_variables_1962():
    from src.leetcode_1962_remove_stones_to_minimize_the_total import Solution

    solution = Solution()

    def _init_variables_1962():
        return solution

    yield _init_variables_1962


class TestClass1962:
    def test_solution_0(self, init_variables_1962):
        assert init_variables_1962().minStoneSum([5, 4, 9], 2) == 12

    def test_solution_1(self, init_variables_1962):
        assert init_variables_1962().minStoneSum([4, 3, 6, 7], 3) == 12
