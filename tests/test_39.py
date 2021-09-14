#!/usr/bin/env python

import pytest

"""
Test 39. Combination Sum
"""


@pytest.fixture(scope="session")
def init_variables_39():
    from src.leetcode_39_combination_sum import Solution

    solution = Solution()

    def _init_variables_39():
        return solution

    yield _init_variables_39


class TestClass39:
    def test_solution_0(self, init_variables_39):
        assert init_variables_39().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]

    def test_solution_1(self, init_variables_39):
        assert init_variables_39().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    def test_solution_2(self, init_variables_39):
        assert init_variables_39().combinationSum([2], 1) == []

    def test_solution_3(self, init_variables_39):
        assert init_variables_39().combinationSum([1], 1) == [[1]]

    def test_solution_4(self, init_variables_39):
        assert init_variables_39().combinationSum([1], 2) == [[1, 1]]


#!/usr/bin/env python

import pytest

"""
Test 39. Combination Sum
"""


@pytest.fixture(scope="session")
def init_variables_39():
    from src.leetcode_39_combination_sum import Solution

    solution = Solution()

    def _init_variables_39():
        return solution

    yield _init_variables_39


class TestClass39:
    def test_solution_0(self, init_variables_39):
        assert init_variables_39().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]

    def test_solution_1(self, init_variables_39):
        assert init_variables_39().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    def test_solution_2(self, init_variables_39):
        assert init_variables_39().combinationSum([2], 1) == []

    def test_solution_3(self, init_variables_39):
        assert init_variables_39().combinationSum([1], 1) == [[1]]

    def test_solution_4(self, init_variables_39):
        assert init_variables_39().combinationSum([1], 2) == [[1, 1]]
