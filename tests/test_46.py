#!/usr/bin/env python

import pytest

"""
Test 46. Permutations
"""


@pytest.fixture(scope="session")
def init_variables_46():
    from src.leetcode_46_permutations import Solution

    solution = Solution()

    def _init_variables_46():
        return solution

    yield _init_variables_46


class TestClass46:
    def test_solution_0(self, init_variables_46):
        assert init_variables_46().permute([1, 2, 3]) == [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]

    def test_solution_1(self, init_variables_46):
        assert init_variables_46().permute([0, 1]) == [[0, 1], [1, 0]]

    def test_solution_2(self, init_variables_46):
        assert init_variables_46().permute([1]) == [[1]]


#!/usr/bin/env python

import pytest

"""
Test 46. Permutations
"""


@pytest.fixture(scope="session")
def init_variables_46():
    from src.leetcode_46_permutations import Solution

    solution = Solution()

    def _init_variables_46():
        return solution

    yield _init_variables_46


class TestClass46:
    def test_solution_0(self, init_variables_46):
        assert init_variables_46().permute([1, 2, 3]) == [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]

    def test_solution_1(self, init_variables_46):
        assert init_variables_46().permute([0, 1]) == [[0, 1], [1, 0]]

    def test_solution_2(self, init_variables_46):
        assert init_variables_46().permute([1]) == [[1]]
