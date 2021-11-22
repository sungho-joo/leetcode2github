#!/usr/bin/env python

import pytest

"""
Test 41. First Missing Positive
"""


@pytest.fixture(scope="session")
def init_variables_41():
    from src.leetcode_41_first_missing_positive import Solution

    solution = Solution()

    def _init_variables_41():
        return solution

    yield _init_variables_41


class TestClass41:
    def test_solution_0(self, init_variables_41):
        assert init_variables_41().firstMissingPositive([1, 2, 0]) == 3

    def test_solution_1(self, init_variables_41):
        assert init_variables_41().firstMissingPositive([3, 4, -1, 1]) == 2

    def test_solution_2(self, init_variables_41):
        assert init_variables_41().firstMissingPositive([7, 8, 9, 11, 12]) == 1
