#!/usr/bin/env python

import pytest

"""
Test 565. Array Nesting
"""


@pytest.fixture(scope="session")
def init_variables_565():
    from src.leetcode_565_array_nesting import Solution

    solution = Solution()

    def _init_variables_565():
        return solution

    yield _init_variables_565


class TestClass565:
    def test_solution_0(self, init_variables_565):
        assert init_variables_565().arrayNesting([5, 4, 0, 3, 1, 6, 2]) == 4

    def test_solution_1(self, init_variables_565):
        assert init_variables_565().arrayNesting([0, 1, 2]) == 1
