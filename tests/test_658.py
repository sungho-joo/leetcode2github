#!/usr/bin/env python

import pytest

"""
Test 658. Find K Closest Elements
"""


@pytest.fixture(scope="session")
def init_variables_658():
    from src.leetcode_658_find_k_closest_elements import Solution

    solution = Solution()

    def _init_variables_658():
        return solution

    yield _init_variables_658


class TestClass658:
    def test_solution_0(self, init_variables_658):
        assert init_variables_658().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

    def test_solution_1(self, init_variables_658):
        assert init_variables_658().findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]


#!/usr/bin/env python

import pytest

"""
Test 658. Find K Closest Elements
"""


@pytest.fixture(scope="session")
def init_variables_658():
    from src.leetcode_658_find_k_closest_elements import Solution

    solution = Solution()

    def _init_variables_658():
        return solution

    yield _init_variables_658


class TestClass658:
    def test_solution_0(self, init_variables_658):
        assert init_variables_658().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

    def test_solution_1(self, init_variables_658):
        assert init_variables_658().findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
