#!/usr/bin/env python

import pytest

"""
Test 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
"""


@pytest.fixture(scope="session")
def init_variables_1438():
    from src.leetcode_1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1438():
        return solution

    yield _init_variables_1438


class TestClass1438:
    def test_solution_0(self, init_variables_1438):
        assert init_variables_1438().longestSubarray([8, 2, 4, 7], 4) == 2

    def test_solution_1(self, init_variables_1438):
        assert init_variables_1438().longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4

    def test_solution_2(self, init_variables_1438):
        assert init_variables_1438().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3
