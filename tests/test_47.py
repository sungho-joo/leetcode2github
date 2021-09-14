#!/usr/bin/env python

import pytest

"""
Test 47. Permutations II
"""


@pytest.fixture(scope="session")
def init_variables_47():
    from src.leetcode_47_permutations_ii import Solution

    solution = Solution()

    def _init_variables_47():
        return solution

    yield _init_variables_47


class TestClass47:
    def test_solution_0(self, init_variables_47):
        assert init_variables_47().permuteUnique([1, 1, 2]) == [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]


#!/usr/bin/env python

import pytest

"""
Test 47. Permutations II
"""


@pytest.fixture(scope="session")
def init_variables_47():
    from src.leetcode_47_permutations_ii import Solution

    solution = Solution()

    def _init_variables_47():
        return solution

    yield _init_variables_47


class TestClass47:
    def test_solution_0(self, init_variables_47):
        assert init_variables_47().permuteUnique([1, 1, 2]) == [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
