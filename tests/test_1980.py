#!/usr/bin/env python

import pytest

"""
Test 1980. Find Unique Binary String
"""


@pytest.fixture(scope="session")
def init_variables_1980():
    from src.leetcode_1980_find_unique_binary_string import Solution

    solution = Solution()

    def _init_variables_1980():
        return solution

    yield _init_variables_1980


class TestClass1980:
    def test_solution_0(self, init_variables_1980):
        assert init_variables_1980().findDifferentBinaryString(["01", "10"]) == "11"

    def test_solution_1(self, init_variables_1980):
        assert init_variables_1980().findDifferentBinaryString(["00", "01"]) == "11"

    def test_solution_2(self, init_variables_1980):
        assert init_variables_1980().findDifferentBinaryString(["111", "011", "001"]) == "101"
