#!/usr/bin/env python

import pytest

"""
Test 66. Plus One
"""


@pytest.fixture(scope="session")
def init_variables_66():
    from src.leetcode_66_plus_one import Solution

    solution = Solution()

    def _init_variables_66():
        return solution

    yield _init_variables_66


class TestClass66:
    def test_solution_0(self, init_variables_66):
        assert init_variables_66().plusOne([1, 2, 3]) == [1, 2, 4]

    def test_solution_1(self, init_variables_66):
        assert init_variables_66().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

    def test_solution_2(self, init_variables_66):
        assert init_variables_66().plusOne([0]) == [1]

    def test_solution_3(self, init_variables_66):
        assert init_variables_66().plusOne([9]) == [1, 0]
