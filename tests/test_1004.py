#!/usr/bin/env python

import pytest

"""
Test 1004. Max Consecutive Ones III
"""


@pytest.fixture(scope="session")
def init_variables_1004():
    from src.leetcode_1004_max_consecutive_ones_iii import Solution

    solution = Solution()

    def _init_variables_1004():
        return solution

    yield _init_variables_1004


class TestClass1004:
    def test_solution_0(self, init_variables_1004):
        assert init_variables_1004().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6

    def test_solution_1(self, init_variables_1004):
        assert (
            init_variables_1004().longestOnes(
                [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
            )
            == 10
        )
