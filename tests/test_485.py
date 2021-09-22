#!/usr/bin/env python

import pytest

"""
Test 485. Max Consecutive Ones
"""


@pytest.fixture(scope="session")
def init_variables_485():
    from src.leetcode_485_max_consecutive_ones import Solution

    solution = Solution()

    def _init_variables_485():
        return solution

    yield _init_variables_485


class TestClass485:
    def test_solution_0(self, init_variables_485):
        assert init_variables_485().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3

    def test_solution_1(self, init_variables_485):
        assert init_variables_485().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
