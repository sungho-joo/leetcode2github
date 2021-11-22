#!/usr/bin/env python

import pytest

"""
Test 43. Multiply Strings
"""


@pytest.fixture(scope="session")
def init_variables_43():
    from src.leetcode_43_multiply_strings import Solution

    solution = Solution()

    def _init_variables_43():
        return solution

    yield _init_variables_43


class TestClass43:
    def test_solution_0(self, init_variables_43):
        assert init_variables_43().multiply("2", "3") == "6"

    def test_solution_1(self, init_variables_43):
        assert init_variables_43().multiply("123", "456") == "56088"
