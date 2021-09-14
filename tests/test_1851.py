#!/usr/bin/env python

import pytest

"""
Test 1851. Minimum Interval to Include Each Query
"""


@pytest.fixture(scope="session")
def init_variables_1851():
    from src.leetcode_1851_minimum_interval_to_include_each_query import Solution

    solution = Solution()

    def _init_variables_1851():
        return solution

    yield _init_variables_1851


class TestClass1851:
    def test_solution_0(self, init_variables_1851):
        assert init_variables_1851().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [
            3,
            3,
            1,
            4,
        ]

    def test_solution_1(self, init_variables_1851):
        assert init_variables_1851().minInterval(
            [[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]
        ) == [2, -1, 4, 6]


#!/usr/bin/env python

import pytest

"""
Test 1851. Minimum Interval to Include Each Query
"""


@pytest.fixture(scope="session")
def init_variables_1851():
    from src.leetcode_1851_minimum_interval_to_include_each_query import Solution

    solution = Solution()

    def _init_variables_1851():
        return solution

    yield _init_variables_1851


class TestClass1851:
    def test_solution_0(self, init_variables_1851):
        assert init_variables_1851().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [
            3,
            3,
            1,
            4,
        ]

    def test_solution_1(self, init_variables_1851):
        assert init_variables_1851().minInterval(
            [[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]
        ) == [2, -1, 4, 6]
