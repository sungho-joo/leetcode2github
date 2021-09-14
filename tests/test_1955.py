#!/usr/bin/env python

import pytest

"""
Test 1955. Count Number of Special Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_1955():
    from src.leetcode_1955_count_number_of_special_subsequences import Solution

    solution = Solution()

    def _init_variables_1955():
        return solution

    yield _init_variables_1955


class TestClass1955:
    def test_solution_0(self, init_variables_1955):
        assert init_variables_1955().countSpecialSubsequences([0, 1, 2, 2]) == 3

    def test_solution_1(self, init_variables_1955):
        assert init_variables_1955().countSpecialSubsequences([2, 2, 0, 0]) == 0

    def test_solution_2(self, init_variables_1955):
        assert init_variables_1955().countSpecialSubsequences([0, 1, 2, 0, 1, 2]) == 7


#!/usr/bin/env python

import pytest

"""
Test 1955. Count Number of Special Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_1955():
    from src.leetcode_1955_count_number_of_special_subsequences import Solution

    solution = Solution()

    def _init_variables_1955():
        return solution

    yield _init_variables_1955


class TestClass1955:
    def test_solution_0(self, init_variables_1955):
        assert init_variables_1955().countSpecialSubsequences([0, 1, 2, 2]) == 3

    def test_solution_1(self, init_variables_1955):
        assert init_variables_1955().countSpecialSubsequences([2, 2, 0, 0]) == 0

    def test_solution_2(self, init_variables_1955):
        assert init_variables_1955().countSpecialSubsequences([0, 1, 2, 0, 1, 2]) == 7
