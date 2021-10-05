#!/usr/bin/env python

import pytest

"""
Test 922. Sort Array By Parity II
"""


@pytest.fixture(scope="session")
def init_variables_922():
    from src.leetcode_922_sort_array_by_parity_ii import Solution

    solution = Solution()

    def _init_variables_922():
        return solution

    yield _init_variables_922


class TestClass922:
    def test_solution_0(self, init_variables_922):
        assert init_variables_922().sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7]

    def test_solution_1(self, init_variables_922):
        assert init_variables_922().sortArrayByParityII([2, 3]) == [2, 3]
