#!/usr/bin/env python

import pytest

"""
Test 1906. Minimum Absolute Difference Queries
"""


@pytest.fixture(scope="session")
def init_variables_1906():
    from src.leetcode_1906_minimum_absolute_difference_queries import Solution

    solution = Solution()

    def _init_variables_1906():
        return solution

    yield _init_variables_1906


class TestClass1906:
    def test_solution_0(self, init_variables_1906):
        assert init_variables_1906().minDifference([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]) == [
            2,
            1,
            4,
            1,
        ]

    def test_solution_1(self, init_variables_1906):
        assert init_variables_1906().minDifference(
            [4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]]
        ) == [-1, 1, 1, 3]


#!/usr/bin/env python

import pytest

"""
Test 1906. Minimum Absolute Difference Queries
"""


@pytest.fixture(scope="session")
def init_variables_1906():
    from src.leetcode_1906_minimum_absolute_difference_queries import Solution

    solution = Solution()

    def _init_variables_1906():
        return solution

    yield _init_variables_1906


class TestClass1906:
    def test_solution_0(self, init_variables_1906):
        assert init_variables_1906().minDifference([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]) == [
            2,
            1,
            4,
            1,
        ]

    def test_solution_1(self, init_variables_1906):
        assert init_variables_1906().minDifference(
            [4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]]
        ) == [-1, 1, 1, 3]
