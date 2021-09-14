#!/usr/bin/env python

import pytest

"""
Test 90. Subsets II
"""


@pytest.fixture(scope="session")
def init_variables_90():
    from src.leetcode_90_subsets_ii import Solution

    solution = Solution()

    def _init_variables_90():
        return solution

    yield _init_variables_90


class TestClass90:
    def test_solution_0(self, init_variables_90):
        assert init_variables_90().subsetsWithDup([1, 2, 2]) == [
            [],
            [1],
            [1, 2],
            [1, 2, 2],
            [2],
            [2, 2],
        ]

    def test_solution_1(self, init_variables_90):
        assert init_variables_90().subsetsWithDup([0]) == [[], [0]]


#!/usr/bin/env python

import pytest

"""
Test 90. Subsets II
"""


@pytest.fixture(scope="session")
def init_variables_90():
    from src.leetcode_90_subsets_ii import Solution

    solution = Solution()

    def _init_variables_90():
        return solution

    yield _init_variables_90


class TestClass90:
    def test_solution_0(self, init_variables_90):
        assert init_variables_90().subsetsWithDup([1, 2, 2]) == [
            [],
            [1],
            [1, 2],
            [1, 2, 2],
            [2],
            [2, 2],
        ]

    def test_solution_1(self, init_variables_90):
        assert init_variables_90().subsetsWithDup([0]) == [[], [0]]
