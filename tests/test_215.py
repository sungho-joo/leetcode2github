#!/usr/bin/env python

import pytest

"""
Test 215. Kth Largest Element in an Array
"""


@pytest.fixture(scope="session")
def init_variables_215():
    from src.leetcode_215_kth_largest_element_in_an_array import Solution

    solution = Solution()

    def _init_variables_215():
        return solution

    yield _init_variables_215


class TestClass215:
    def test_solution_0(self, init_variables_215):
        assert init_variables_215().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_solution_1(self, init_variables_215):
        assert init_variables_215().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
