#!/usr/bin/env python

import pytest

"""
Test 217. Contains Duplicate
"""


@pytest.fixture(scope="session")
def init_variables_217():
    from src.leetcode_217_contains_duplicate import Solution

    solution = Solution()

    def _init_variables_217():
        return solution

    yield _init_variables_217


class TestClass217:
    def test_solution_0(self, init_variables_217):
        assert init_variables_217().containsDuplicate([1, 2, 3, 1])

    def test_solution_1(self, init_variables_217):
        assert not init_variables_217().containsDuplicate([1, 2, 3, 4])

    def test_solution_2(self, init_variables_217):
        assert init_variables_217().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
