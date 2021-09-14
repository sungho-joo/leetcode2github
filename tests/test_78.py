#!/usr/bin/env python

import pytest

"""
Test 78. Subsets
"""


@pytest.fixture(scope="session")
def init_variables_78():
    from src.leetcode_78_subsets import Solution

    solution = Solution()

    def _init_variables_78():
        return solution

    yield _init_variables_78


class TestClass78:
    def test_solution_0(self, init_variables_78):
        assert init_variables_78().subsets([1, 2, 3]) == [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]

    def test_solution_1(self, init_variables_78):
        assert init_variables_78().subsets([0]) == [[], [0]]


#!/usr/bin/env python

import pytest

"""
Test 78. Subsets
"""


@pytest.fixture(scope="session")
def init_variables_78():
    from src.leetcode_78_subsets import Solution

    solution = Solution()

    def _init_variables_78():
        return solution

    yield _init_variables_78


class TestClass78:
    def test_solution_0(self, init_variables_78):
        assert init_variables_78().subsets([1, 2, 3]) == [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]

    def test_solution_1(self, init_variables_78):
        assert init_variables_78().subsets([0]) == [[], [0]]
