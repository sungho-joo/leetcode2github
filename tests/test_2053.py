#!/usr/bin/env python

import pytest

"""
Test 2053. Kth Distinct String in an Array
"""


@pytest.fixture(scope="session")
def init_variables_2053():
    from src.leetcode_2053_kth_distinct_string_in_an_array import Solution

    solution = Solution()

    def _init_variables_2053():
        return solution

    yield _init_variables_2053


class TestClass2053:
    def test_solution_0(self, init_variables_2053):
        assert init_variables_2053().kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"

    def test_solution_1(self, init_variables_2053):
        assert init_variables_2053().kthDistinct(["aaa", "aa", "a"], 1) == "aaa"

    def test_solution_2(self, init_variables_2053):
        assert init_variables_2053().kthDistinct(["a", "b", "a"], 3) == ""
