#!/usr/bin/env python

import pytest

"""
Test 230. Kth Smallest Element in a BST
"""


@pytest.fixture(scope="session")
def init_variables_230():
    from src.leetcode_230_kth_smallest_element_in_a_bst import Solution

    solution = Solution()

    def _init_variables_230():
        return solution

    yield _init_variables_230


class TestClass230:
    def test_solution_0(self, init_variables_230):
        assert init_variables_230().kthSmallest([3, 1, 4, None, 2], 1) == 1

    def test_solution_1(self, init_variables_230):
        assert init_variables_230().kthSmallest([5, 3, 6, 2, 4, None, None, 1], 3) == 3
