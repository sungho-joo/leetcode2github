#!/usr/bin/env python

import pytest

"""
Test 2070. Most Beautiful Item for Each Query
"""


@pytest.fixture(scope="session")
def init_variables_2070():
    from src.leetcode_2070_most_beautiful_item_for_each_query import Solution

    solution = Solution()

    def _init_variables_2070():
        return solution

    yield _init_variables_2070


class TestClass2070:
    def test_solution_0(self, init_variables_2070):
        assert init_variables_2070().maximumBeauty(
            [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
        ) == [2, 4, 5, 5, 6, 6]

    def test_solution_1(self, init_variables_2070):
        assert init_variables_2070().maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], [1]) == [4]

    def test_solution_2(self, init_variables_2070):
        assert init_variables_2070().maximumBeauty([[10, 1000]], [5]) == [0]
