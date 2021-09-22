#!/usr/bin/env python

import pytest

"""
Test 2009. Minimum Number of Operations to Make Array Continuous
"""


@pytest.fixture(scope="session")
def init_variables_2009():
    from src.leetcode_2009_minimum_number_of_operations_to_make_array_continuous import (
        Solution,
    )

    solution = Solution()

    def _init_variables_2009():
        return solution

    yield _init_variables_2009


class TestClass2009:
    def test_solution_0(self, init_variables_2009):
        assert init_variables_2009().minOperations([4, 2, 5, 3]) == 0

    def test_solution_1(self, init_variables_2009):
        assert init_variables_2009().minOperations([1, 2, 3, 5, 6]) == 1

    def test_solution_2(self, init_variables_2009):
        assert init_variables_2009().minOperations([1, 10, 100, 1000]) == 3
