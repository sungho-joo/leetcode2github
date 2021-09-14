#!/usr/bin/env python

import pytest

"""
Test 53. Maximum Subarray
"""


@pytest.fixture(scope="session")
def init_variables_53():
    from src.leetcode_53_maximum_subarray import Solution

    solution = Solution()

    def _init_variables_53():
        return solution

    yield _init_variables_53


class TestClass53:
    def test_solution_0(self, init_variables_53):
        assert init_variables_53().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_solution_1(self, init_variables_53):
        assert init_variables_53().maxSubArray([1]) == 1

    def test_solution_2(self, init_variables_53):
        assert init_variables_53().maxSubArray([5, 4, -1, 7, 8]) == 23
