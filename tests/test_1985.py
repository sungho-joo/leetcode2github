#!/usr/bin/env python

import pytest

"""
Test 1985. Find the Kth Largest Integer in the Array
"""


@pytest.fixture(scope="session")
def init_variables_1985():
    from src.leetcode_1985_find_the_kth_largest_integer_in_the_array import Solution

    solution = Solution()

    def _init_variables_1985():
        return solution

    yield _init_variables_1985


class TestClass1985:
    def test_solution_0(self, init_variables_1985):
        assert init_variables_1985().kthLargestNumber(["3", "6", "7", "10"], 4) == "3"

    def test_solution_1(self, init_variables_1985):
        assert init_variables_1985().kthLargestNumber(["2", "21", "12", "1"], 3) == "2"

    def test_solution_2(self, init_variables_1985):
        assert init_variables_1985().kthLargestNumber(["0", "0"], 2) == "0"
