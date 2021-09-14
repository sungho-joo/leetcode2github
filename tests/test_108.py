#!/usr/bin/env python

import pytest

"""
Test 108. Convert Sorted Array to Binary Search Tree
"""


@pytest.fixture(scope="session")
def init_variables_108():
    from src.leetcode_108_convert_sorted_array_to_binary_search_tree import Solution

    solution = Solution()

    def _init_variables_108():
        return solution

    yield _init_variables_108


class TestClass108:
    def test_solution_0(self, init_variables_108):
        assert init_variables_108().sortedArrayToBST([-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5]

    def test_solution_1(self, init_variables_108):
        assert init_variables_108().sortedArrayToBST([1, 3]) == [3, 1]
