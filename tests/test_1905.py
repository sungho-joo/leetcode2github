#!/usr/bin/env python

import pytest

"""
Test 1905. Count Sub Islands
"""


@pytest.fixture(scope="session")
def init_variables_1905():
    from src.leetcode_1905_count_sub_islands import Solution

    solution = Solution()

    def _init_variables_1905():
        return solution

    yield _init_variables_1905


class TestClass1905:
    def test_solution_0(self, init_variables_1905):
        assert (
            init_variables_1905().countSubIslands(
                [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],
            )
            == 3
        )

    def test_solution_1(self, init_variables_1905):
        assert (
            init_variables_1905().countSubIslands(
                [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]],
            )
            == 2
        )


#!/usr/bin/env python

import pytest

"""
Test 1905. Count Sub Islands
"""


@pytest.fixture(scope="session")
def init_variables_1905():
    from src.leetcode_1905_count_sub_islands import Solution

    solution = Solution()

    def _init_variables_1905():
        return solution

    yield _init_variables_1905


class TestClass1905:
    def test_solution_0(self, init_variables_1905):
        assert (
            init_variables_1905().countSubIslands(
                [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],
            )
            == 3
        )

    def test_solution_1(self, init_variables_1905):
        assert (
            init_variables_1905().countSubIslands(
                [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]],
            )
            == 2
        )
