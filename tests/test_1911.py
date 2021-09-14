#!/usr/bin/env python

import pytest

"""
Test 1911. Maximum Alternating Subsequence Sum
"""


@pytest.fixture(scope="session")
def init_variables_1911():
    from src.leetcode_1911_maximum_alternating_subsequence_sum import Solution

    solution = Solution()

    def _init_variables_1911():
        return solution

    yield _init_variables_1911


class TestClass1911:
    def test_solution_0(self, init_variables_1911):
        assert init_variables_1911().maxAlternatingSum([4, 2, 5, 3]) == 7

    def test_solution_1(self, init_variables_1911):
        assert init_variables_1911().maxAlternatingSum([5, 6, 7, 8]) == 8

    def test_solution_2(self, init_variables_1911):
        assert init_variables_1911().maxAlternatingSum([6, 2, 1, 2, 4, 5]) == 10


#!/usr/bin/env python

import pytest

"""
Test 1911. Maximum Alternating Subsequence Sum
"""


@pytest.fixture(scope="session")
def init_variables_1911():
    from src.leetcode_1911_maximum_alternating_subsequence_sum import Solution

    solution = Solution()

    def _init_variables_1911():
        return solution

    yield _init_variables_1911


class TestClass1911:
    def test_solution_0(self, init_variables_1911):
        assert init_variables_1911().maxAlternatingSum([4, 2, 5, 3]) == 7

    def test_solution_1(self, init_variables_1911):
        assert init_variables_1911().maxAlternatingSum([5, 6, 7, 8]) == 8

    def test_solution_2(self, init_variables_1911):
        assert init_variables_1911().maxAlternatingSum([6, 2, 1, 2, 4, 5]) == 10
